	.data
	.text
	.globl main 
	
main:
	li $t1,0
	li $t2,0
	
	li $v0,5
	syscall
	move $t0,$v0
	
for:
    	bge $t2,32,endfor
    
    	andi $t3,$t0,1
    
    	beq $t3,0,endif
    
    	addi $t1,$t1,1
    
endif:
	srl $t0,$t0,1
	addi $t2,$t2,1
    	j for
    	
endfor:
    	# Imprimir soma
    	move $a0,$t1
    	li $v0,1
    	syscall
    	
    	jr $ra