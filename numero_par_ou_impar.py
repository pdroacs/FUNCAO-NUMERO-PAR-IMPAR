def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


# Pegando o número do usuário
numero_usuario = int(input("Digite um número: "))
resultado = par_impar(numero_usuario)

print(resultado)
