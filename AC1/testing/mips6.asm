	.data
	.text
	.globl main
	
main:
	li $t0,0
	li $t1,0
	
while:
	bge $t0,5,endw
	
	add $t1,$t1,$t0
	addi $t0,$t0,1
	
	j while
	
endw:
	move $a0,$t1
	li $v0,1
	syscall
	
	jr $ra