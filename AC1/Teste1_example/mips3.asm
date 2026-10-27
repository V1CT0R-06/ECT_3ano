	.eqv SIZE,5

	.data
array: .word 12, -3, 7, 20, 4

	.text
	.globl main

main:
    li $t1,0
    la $t0,array
    lw $t2,0($t0)
    
    move $t4,$t0
    addiu $t4,$t4,20
    
for:
    bgeu $t0,$t4,endfor
    lw $t3,0($t0)
    add $t1,$t1,$t3
    
    ble $t3,$t2,endif
    move $t2,$t3
    
endif:
    addiu $t0,$t0,4
    j for

endfor:
    # Imprimir soma
    move $a0,$t1
    li $v0,1
    syscall

    # Imprimir maior
    move $a0,$t2
    li $v0,1
    syscall

    jr $ra