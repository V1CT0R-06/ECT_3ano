
	.eqv N,35

	.data
a: .space 140
b: .space 140

	.text
	.globl main

main:
    li $t0,0
    li $t1,0

    la $t4,a
    la $t5,b
    addiu $t6,$t4,140

    move $t2,$t4

for_read:
    bgeu $t2,$t6,endfor_read

    li $v0,5
    syscall
    sw $v0,0($t2)

    addiu $t2,$t2,4
    j for_read

endfor_read:
    move $t2,$t4
    move $t3,$t5

for_separate:
    bgeu $t2,$t6,endfor_separate

    lw $t7,0($t2)
    andi $t8,$t7,1

    beq $t8,$zero,else

    sw $t7,0($t3)
    addiu $t3,$t3,4
    addiu $t1,$t1,1
    j endif

else:
    addiu $t0,$t0,1

endif:
    addiu $t2,$t2,4
    j for_separate

endfor_separate:
    move $t3,$t5

    sll $t8,$t1,2
    addu $t9,$t5,$t8

for_print:
    bgeu $t3,$t9,endfor_print

    lw $a0,0($t3)
    li $v0,1
    syscall

    addiu $t3,$t3,4
    j for_print

endfor_print:
    jr $ra
