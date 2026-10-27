
	.eqv SIZE,10
	.eqv TRUE,1
	.eqv FALSE,0
	.eqv print_str,4
	.eqv read_int,5
	.eqv print_int10,1

	.data
	.align 2
lista: .space 40
str1: .asciiz "Introduza um numero: "
str2: .asciiz "\nArray ordenado:\n"
str3: .asciiz "; "
	
	.text
	.globl main

main:
    li $t0,0

read:
    bge $t0,SIZE,endread

    la $a0,str1
    li $v0,print_str
    syscall

    li $v0,read_int
    syscall

    la $t1,lista
    sll $t2,$t0,2
    addu $t2,$t1,$t2
    sw $v0,0($t2)

    addi $t0,$t0,1
    j read

endread:
    la $t6,lista

do:
    li $t4,FALSE
    li $t5,0

for:
    bge $t5,9,endfor

    sll $t7,$t5,2
    addu $t7,$t6,$t7

    lw $t8,0($t7)
    lw $t9,4($t7)

    ble $t8,$t9,endif

    sw $t8,4($t7)
    sw $t9,0($t7)

    li $t4,TRUE

endif:
    addi $t5,$t5,1
    j for

endfor:
    beq $t4,TRUE,do

    la $a0,str2
    li $v0,print_str
    syscall

    la $t0,lista
    li $t2,SIZE
    sll $t2,$t2,2
    addu $t2,$t0,$t2

print:
    bgeu $t0,$t2,endprint

    lw $t1,0($t0)

    or $a0,$t1,$0
    li $v0,print_int10
    syscall

    la $a0,str3
    li $v0,print_str
    syscall

    addiu $t0,$t0,4
    j print

endprint:
    jr $ra
