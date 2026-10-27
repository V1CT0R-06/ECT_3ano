	.data
	.text
	.globl main
	
main:
	li $t0,0
	li $t1,0
	li $t2,0
	
for:
	bge $t0,5,endfor
	
	li $v0,5
	syscall
	move $t1,$v0
	
if:
	bge $t1,0,endif
	add $t2,$t2,$t1
	
endif:
	addi $t0,$t0,1
	
	j for
	
endfor:

	move $a0,$t2
	li $v0,1
	syscall
	
	jr $ra