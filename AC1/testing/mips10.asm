	.data
array: .word 5,8,3,10

	.text
	.globl main

main:
    	la $t0,array
    	lw $t2,0($t0)
    	li $t3,0
    	

while:
	bge $t3,4,endw
	
	lw $t1,0($t0)
	
	bge $t1,$t2,endif
	move $t2,$t1

endif:
	addiu $t0,$t0,4
	addi $t3,$t3,1
		
	j while
endw:
    	move $a0,$t2
    	li $v0,1
    	syscall
    
    	jr $ra