	.data
array: .word 5,-2,3,1
	.text
	.globl main
	.eqv FALSE,0
	.eqv TRUE,1
	.eqv SIZE,10
	
main:	
	la $t6,array #lista
	
do: 
	li $t4,FALSE #comeca falso em alteracoes
	li $t5,0 # i
	
for:
	bge $t5,3,endfor
	
if:
	sll $t7,$t5,2 #endereco 7 para o sll
	addu $t3,$t6,$t7
	
	lw $t8,0($t3)
	lw $t9,4($t3)
	
	bleu $t8,$t9,endif
	
	sw $t9,0($t3)
	sw $t8,4($t3)
	
	li $t4,TRUE #quando altera fica true
	
endif:
	addi $t5,$t5,1
	j for
	
endfor:
	beq $t4,TRUE,do
	
	jr $ra