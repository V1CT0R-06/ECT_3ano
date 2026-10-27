	.data
val: 	.word 8,4,15,-1987,327,-9,27,16
str1: .asciiz "Result is: "
	.text
	.globl main
	.eqv SIZE,8
	
main:
	li $t0,0
	la $t2,val
	
do:
	sll $t4,$t0,2
	addu $t5,$t2,$t4
	
	lw $t1,0($t5)
	lw $t6,16($t5)
	
	sw $t6,0($t5)
	sw $t1,16($t5)
	
	addiu $t0,$t0,1
	
	blt $t0,4,do
	
enddo:
	la $a0,str1
	li $v0,4
	syscall
	
	move $t3,$t2
	addiu $t7,$t2,32
	
while:
    bgeu $t3,$t7,endw

    lw $a0,0($t3)
    li $v0,1
    syscall

    addiu $t3,$t3,4

    li $a0,','
    li $v0,11
    syscall

    j while

endw:
    jr $ra
	