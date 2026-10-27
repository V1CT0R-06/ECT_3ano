
	.data

	.text
	.globl main

main:
    li $t0, 0 
    li $t2, 0 #soma
    li $t3, 0 #contagem

for:
    bge $t0,8,endfor
    
    li $v0, 5
    syscall
    move $t1,$v0
    ble $t1,0,endif
    rem $t4,$t1,2
    bne $t4,0,endif
    
    add $t2,$t2,$t1 #somar
    
    
    addi $t3,$t3,1 #contar
    
endif:
    addi $t0,$t0,1 #contagem do i
    j for 

endfor: #acaba o ciclo for

    move $a0,$t2
    li $v0,1
    syscall
    
    move $a0,$t3
    li $v0,1
    syscall

    jr $ra