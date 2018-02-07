
.data
	pin: .int 18
	delay_time: .int 1
	output: .int 1
	GPIO_BASE: .long 0x3F200000
	FUN_SEL_OFFSET: .int 0x0
	SET_OFFSET: .int 0x1C
	CLEAR_OFFSET: .int 0x28
	fileName: .asciz "/dev/mem"
	MAP_SHARED: .int 1
	MAP_FAILED: .word -1
	PROT_READ: .int 1
	PROT_WRITE: .int 2
	O_RDWR: .int 2
	openFailed: .asciz "open() failed\n"
	mapFailed: .asciz "mmap() failed\n"
	starting: .asciz "Program Starting\n"
	doneSetup: .asciz "Done with Setup\n"
	doneSetPinMOde: .asciz "Done with Setting Pin Mode\n"

.text
	.global main
	.extern printf
	.extern sleep

main:
	push {ip, lr} @stores information needed when the program exits
	ldr r0, =starting
	bl printf
	ldr r1, =O_RDWR
	ldr r1, [r1]
	ldr r0, =fileName
	bl open
	mov r11, r0 @save the file discriptor
	subs r0, r0, #-1 @will set flags based on the subtraction
	beq openError @if r0 == -1 go to openError
	sub sp, sp, #8
	ldr r0, =GPIO_BASE
	ldr r0, [r0]
	str r0, [sp, #4]
	str r11, [sp]
	ldr r3, =MAP_SHARED
	ldr r3, [r3]
	ldr r2, =PROT_READ
	ldr r2, [r2]
	ldr r0, =PROT_WRITE
	ldr r0, [r0]
	orr r2, r2, r0
	mov r1, #4096
	mov r0, #0
	bl mmap
	add sp, sp, #8
	ldr r1, =MAP_FAILED
	ldr r1, [r1]
	subs r1, r0, r1 @will set flags based on the subtraction
	beq mapError @if r0 == MAP_FAILED go to mapError
	mov r10, r0 @keep gpioBase
	ldr r0, =doneSetup
	bl printf

	@set parameters for setPinMode
	sub sp, sp, #16 @ setup sp to store gpioBase(#0), pin(#4), and delay_time(#8)

	@ seting gpioBase
	mov r0, r10
	str r0, [sp] @ store gpioBase on stack

	@ setting pin
	ldr r1, =pin
	ldr r1, [r1]
	str r1, [sp, #4]

	@here you set output pin
	ldr r2, =output
	ldr r2, [r2]

	@ storing delay_time at sp[8]
	ldr r3, =delay_time
	ldr r3, [r3]
	str r3, [sp, #8]

	bl setPinMode

	ldr r0, =doneSetPinMOde
	bl printf

	mov r7, #0 @ r7(i) = 0

loopStart:
	@complete your loop here
	add r7, r7, #1 @ i++

	@ setup and call pin on
	ldr r0, [sp] @ r0 = gpioBase
	ldr r1, [sp, #4] @ r1 = pin
	bl setPinOn

	@ sleep
	ldr r0, [sp, #8]
	bl sleep

	@ setup and call pin off
	ldr r0, [sp] @ r0 = gpioBase
	ldr r1, [sp, #4] @ r1 = pin
	bl setPinOff

	@ sleep
	ldr r0, [sp, #8]
	bl sleep

	@ check if loop is done
	cmp r7, #10
	bne loopStart
	add sp, sp, #16
	pop {ip, pc}

openError:
	ldr r0, =openFailed
	bl printf
	mov r0, #1 @puts 1 as the return value
	pop {ip, pc}
mapError:
	mov r0, r11
	bl close
	ldr r0, =mapFailed
	bl printf
	mov r0, #1 @puts 1 as the return value
	pop {ip, pc}
modulus:
	push {lr}
	udiv r2, r0, r1
	mls r0, r1, r2, r0
	pop {pc}
setPinMode:
	push {r4-r7, lr}
	ldr r3, =FUN_SEL_OFFSET
	ldr r3, [r3]
	add r4, r0, r3 @r4= gpioBase + FUN_SEL_OFFSET (ie gpioFunSel)
	mov r5, #10
	udiv r6, r1, r5 @r6=pin/10 (ie funSelIndex)
	mov r7, r2 @r7 = mode
	mov r0, r1
	mov r1, r5
	bl modulus @r0 = pin%10
	mov r1, #3
	mul r0, r1, r0 @r0=3*(pin%10) (ie funSelShift)
	ldr r1, [r4, r6, lsl #2] @r1=gpioFunSel[funSelIndex]
	orr r1, r1, r7, lsl r0 @r1= gpioFunSel[funSelIndex] | (mode<<funSelShift)
	str r1, [r4, r6, lsl #2] @write data back to register
	pop {r4-r7, pc}
setPinOn:
	@complete this function
	push {r2-r7, lr}
	ldr r2, =SET_OFFSET
	ldr r2, [r2] @ r2 = mem at SET_OFFSET
	add r3, r0, r2 @ r3 (gpioSet) = gpioBase + SET_OFFSET

	mov r4, #32 @ r4 = 32
	udiv r5, r1, r4 @ r5(gpIOSCIndex) = pin / #32

	sub sp, sp, #8
	str r0, [sp, #4] @ store params on stack
	str r1, [sp]
	mov r0, r1 @ first new param is pin
	mov r1, #32 @ second new param is 32
	bl modulus
	mov r6, r0 @ r6(gpioSCShift) = pin % 32
	ldr r0, [sp, #4]
	ldr r1, [sp]
	add sp, sp, #8

	mov r7, #1
	lsl r7, r7, r6 @ r7(t) = 1 << gpioSCShift

	ldr r2, [r3, r5, lsl #2]
	orr r2, r2, r7
	str r2, [r3, r5, lsl #2]
	pop {r2-r7, pc}

setPinOff:
	@complete this function
	push {r2-r7, lr}
	ldr r2, =CLEAR_OFFSET
	ldr r2, [r2] @ r2 = mem at SET_OFFSET
	add r3, r0, r2 @ r3 (gpioSet) = gpioBase + SET_OFFSET

	mov r4, #32 @ r4 = 32
	udiv r5, r1, r4 @ r5(gpIOSCIndex) = pin / #32

	sub sp, sp, #8
	str r0, [sp, #4] @ store params on stack
	str r1, [sp]
	mov r0, r1 @ first new param is pin
	mov r1, #32 @ second new param is 32
	bl modulus
	mov r6, r0 @ r6(gpioSCShift) = pin % 32
	ldr r0, [sp, #4]
	ldr r1, [sp]
	add sp, sp, #8

	mov r7, #1
	lsl r7, r7, r6 @ r7(t) = 1 << gpioSCShift

	ldr r2, [r3, r5, lsl #2]
	orr r2, r2, r7
	str r2, [r3, r5, lsl #2]
	pop {r2-r7, pc}
