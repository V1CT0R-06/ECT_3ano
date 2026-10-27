	.eqv SIZE,30
	.data
str: .space 31
	.text
	.globl main
	
main:
	li $t0,0
	la $a0,str
	li $a1,SIZE
	li $v0,8
	syscall
	
	la $t1,str
	
while:
	lb $t2,0($t1)
	beq $t2,0,endw
	
	beq $t2,'a',vogal
	beq $t2,'e',vogal
	beq $t2,'i',vogal
	beq $t2,'o',vogal
	beq $t2,'u',vogal
	
	j endif

vogal:
    	addi $t0,$t0,1

endif:
    	addiu $t1,$t1,1
    	j while
    
endw:

	jr $ra