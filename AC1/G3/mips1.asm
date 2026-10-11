	.eqv print_str,4
	.eqv read_int,5
	.eqv print_int10,1

	.data
str1: .asciiz "Introduza um numero: "
str2: .asciiz "Valor ignorado\n"
str3: .asciiz "A soma dos positivos e': "

	.text
	.globl main

main:
    li $t0,0               # soma = 0
    li $t2,0               # i = 0

for:
    bge $t2,5,endfor       # se i >= 5, termina

    la $a0,str1
    li $v0,print_str
    syscall

    li $v0,read_int
    syscall
    or $t1,$v0,$0          

if:
    ble $t1,$0,else       

    add $t0,$t0,$t1        # soma += value
    j endif

else:
    la $a0,str2
    li $v0,print_str
    syscall

endif:
    addi $t2,$t2,1         # i++
    j for

endfor:
    la $a0,str3
    li $v0,print_str
    syscall

    or $a0,$t0,$0
    li $v0,print_int10
    syscall

    jr $ra