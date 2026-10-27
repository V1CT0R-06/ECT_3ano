	.data
array: 	.space 40
	.text
	.globl main
	.eqv FALSE,0
	.eqv TRUE,1
	.eqv SIZE,10
	
main: 
	la $t0,array # &lista[0]
	li $t1,SIZE # SIZE
	addiu $t2,$t1,-1 # SIZE – 1
	sll $t3,$t2,2 # (SIZE – 1) * 4
	
	addu $t6,$t0,$t3 # lista + (SIZE – 1)

do:
	li $t4,FALSE #cena do verdadeiro e falso de alterar
	move $t5,$t0 #ponteiro
	
for:
	bge $t5,$t6,endfor
	
	
if:
	lw $t8, 0($t5) 
	lw $t9, 4($t5)
	ble $t8,$t9,endif
	
	sw $t8,4($t5)
	sw $t9,0($t5)
	
	li $t4,TRUE
	
endif:
	addi $t5,$t5,4
	
	j for
	
endfor:
	beq $t4,TRUE,do
	
	jr $ra