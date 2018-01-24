.data

.balign 4

string: .asciz "a + b = %d\n"

a: .word 33

b: .word 44

c: .word 0

.text
.global main
.extern printf
main:
	push {ip, lr} @ push return address + dummy register
	ldr	r1, =a
	ldr	r1, [r1]
	ldr 	r2, =b
	ldr	r2, [r2]
	add	r1, r1, r2
	ldr	r2, =c
	str	r1, [r2]
	ldr	r0, =string
	ldr	r1, [r2]
	bl	printf
	pop	{ip, pc}
