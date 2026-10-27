
	.eqv SIZE,5
	.eqv print_str,4
	.eqv read_int,5

	.data
lista: .space 20
str: .asciiz "\nIntroduza um numero: "

	.text
	.globl main

main:
    li $t0,0

while:
    bge $t0,SIZE,endw

    la $a0,str
    li $v0,print_str
    syscall

    li $v0,read_int
    syscall

    la $t1,lista
    sll $t2,$t0,2
    addu $t2,$t1,$t2
    sw $v0,0($t2)

    addi $t0,$t0,1
    j while

endw:
    jr $ra