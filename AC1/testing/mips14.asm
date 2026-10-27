	.data
array:	.word 5,8,3,2
	.text
	.globl main
	.eqv TRUE,1
	.eqv FALSE,0
	.eqv SIZE,4
	
main:
	la $t0,array
	li $t1,0
	li $t2,SIZE
	addiu $t3,$t2,-1
	
forex:
	bge $t1,$t3,endforex
	
	addiu $t4,$t1,1
	
forin:
	bge $t4,$t2,endforin
	
	sll $t5,$t1,2
	addu $t6,$t0,$t5
	
	sll $t7,$t4,2
	addu $t8,$t0,$t7
	
	lw $t9,0($t6)
	lw $s0,0($t8)
	
	bge $s0,$t9,endif
	sw $t9,0($t8)
	sw $s0,0($t6)
	
	addiu $t4,$t4,1
	
	j forin
	
endif:
	addiu $t4,$t4,1
	
	j forin
	
endforin:
	addiu $t1,$t1,1
	
	j forex
	
endforex:
	
	jr $ra