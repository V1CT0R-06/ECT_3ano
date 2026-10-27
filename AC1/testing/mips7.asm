	.data
	.text
	.globl main
	
main:
	li $t0,13
	li $t1,0
	
	andi $t1,$t0,1
	
	move $a0,$t1
	li $v0,1
	syscall
	
	jr $ra