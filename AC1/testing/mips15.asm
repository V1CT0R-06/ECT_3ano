	.data
str1: .asciiz "Digite ate 20 inteiros (zero para terminar):"
str2: .asciiz "Maximo/minimo sao: "
	.text
	.globl main
	
main:
	li $t0,0
	li $t1,0x7FFFFFFF
	li $t2,0x80000000
	li $t3,0

	la $a0,str1
	li $v0,4
	syscall

do:	
	li $v0,5
	syscall
	move $t3,$v0
	beq $t3,0,endif
	
	ble $t3,$t2,endifmax
	move $t2,$t3
	
endifmax:
	bge $t3,$t1,endifmin
	move $t1,$t3
	
endifmin:
endif:
	addiu $t0,$t0,1
	
	bge $t0,20,endw
	beq $t3,0,endw
	
	j do

endw:
		
	la $a0,str2
	li $v0,4
	syscall
	
	move $a0,$t2
	li $v0,1
	syscall
	
	li $a0,'/'
	li $v0,11
	syscall

	move $a0,$t1
	li $v0,1
	syscall

	jr $ra