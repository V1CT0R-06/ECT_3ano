	.data 
str: .asciiz "banana"

	.text
	.globl main
	
main:
	la $t0,str
	li $t2,0
	
while:
	lb $t1,0($t0)
	beq $t1,0,endw
	bne $t1,'a',endif
	addi $t2,$t2,1
	
	
endif: 	
	addiu $t0,$t0,1
	j while
	
endw:
	move $a0,$t2
	li $v0,1
	syscall
	
	jr $ra