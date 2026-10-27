	.eqv SIZE,4
	.eqv FALSE,0
	.eqv TRUE,1
	
	.data
array:	.word 5,8,3,2
	.text
	.globl main
	
main:
	la $t0,array
	li $t6,0
	
do:
	li $t6,FALSE
	li $t1,0
	
for:	
	bge $t1,3,endfor
	
	sll $t2,$t1,2
	addu $t3,$t0,$t2
	
	lw $t4,0($t3)
	lw $t5,4($t3)
	
	ble $t4,$t5,endif
	
	sw $t5,0($t3)
	sw $t4,4($t3) 
	
	li $t6,TRUE
	
endif:
	addi $t1,$t1,1
	
	j for

endfor:
	beq $t6,TRUE,do
	jr $ra