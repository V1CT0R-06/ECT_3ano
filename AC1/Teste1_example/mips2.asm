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
	lb $t2, 0($t1)
	beq $t2,0,endwhile
	
	blt $t2,65,endif
	bgt $t2,90,endif
	
    	# cont++
    	addi $t0,$t0,1

endif:
    	# p++
    	addiu $t1,$t1,1

    	# Voltar ao início do while
    	j while

endwhile:
	move $a0,$t0
	li $v0,1
	syscall
	
	jr $ra 