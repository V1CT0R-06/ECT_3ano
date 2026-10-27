	.data
	.text
	.globl main
	
main:
	li $t0,0
	li $t1,0
	
	li $v0,5
	syscall
	move $t0,$v0
	
while:
	beq $t0,0,endw
	
if:
	andi $t2,$t0,1
	beq $t2,0,endif
	
	addi $t1,$t1,1
	
endif:
	srl $t0,$t0,1
	j while
	
endw:
	move $a0,$t1
	li $v0,1
	syscall
	jr $ra