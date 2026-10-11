	.eqv print_str,4
	.eqv read_int,5
	.eqv print_char,11

	.data
str1: .asciiz "Introduza um numero: "
str2: .asciiz "\nO valor em binario e': "

	.text
	.globl main

main:
    la $a0,str1
    li $v0,print_str
    syscall

    li $v0,read_int
    syscall
    or $t0,$v0,$0

    la $a0,str2
    li $v0,print_str
    syscall

    li $t2,0

for:
    bge $t2,32,endfor

    # Espaço de 4 em 4 bits
    rem $t4,$t2,4
    bne $t4,$0,no_space

    li $a0,' '
    li $v0,print_char
    syscall

no_space:
    # Isolar o bit mais à esquerda
    li $t3,0x80000000
    and $t1,$t0,$t3

    # Ver se é 0 ou 1
    beq $t1,$0,else

    li $a0,'1'
    li $v0,print_char
    syscall
    j endif

else:
    li $a0,'0'
    li $v0,print_char
    syscall

endif:
    sll $t0,$t0,1
    addi $t2,$t2,1
    j for

endfor:
    jr $ra