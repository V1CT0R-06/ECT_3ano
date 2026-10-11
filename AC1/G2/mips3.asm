	
	
	.eqv print_str,4
	.eqv read_int,5
	.eqv print_int10,1

	.data
str1: .asciiz "Introduza 2 numeros:\n"
str2: .asciiz "A soma dos dois numeros fica: "

	.text
	.globl main

main:
    la  $a0,str1
    ori $v0,$0,print_str
    syscall

    ori $v0,$0,read_int
    syscall
    or  $t0,$v0,$0

    ori $v0,$0,read_int
    syscall
    or  $t1,$v0,$0

    # mensagem resultado
    la  $a0,str2
    ori $v0,$0,print_str
    syscall

    # conta
    add $t2,$t0,$t1

    # print ao resultado
    or  $a0,$t2,$0
    ori $v0,$0,print_int10
    syscall

    jr $ra