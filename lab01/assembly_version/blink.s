
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

.text
	.global main
	.extern printf

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
	mov r0, r10
	mov r1, #18
	ldr r2, =output
	ldr r2, [r2]
	bl setPinMode
	ldr r0, [sp, #4]
	ldr r11, [sp]
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
	push {r4-r7, lr}
	ldr r3, =SET_OFFSET
	ldr r3, [r3]
	add r4, r0, r3 @r4 = gpioBase + SET_OFFSET (ie gpioSet)
	mov r5, #32
	udiv r6, r1, r5 @ r6=pin/32 (ie gpioSCIndex)
	mov r0, r1
	mov r1, r5
	bl modulus @r0 = pin%32 (ie gpioSCShift)
	mov r3, #1
	lsl r0, r3, r0 @r0 = (1 << gpioSCShift)
	lsl r6, r6, #2
	add r6, r6, r0
	str r0, [r6]
	str r1, [r4, r6, lsl #2] @write data back to register
	pop {r4-r7, pc}
