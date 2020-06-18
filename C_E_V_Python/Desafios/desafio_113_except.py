# DESAFIO 113 - Except
# Reescreva a função leiaInt() que fizemos
# No desafio 104,incluindo agora a possibilidade
# Da digitação de um nùmero de tipo invalido.
# Aproveite e crie também uma função leiaFloot()
# Com a mesma funcionalidade.:)

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO:Por favor, digite um número inteiro válido")
            continue
        else:
            return n

num = leiaInt("Escreva um número inteiro: ")
print(f'O número inteiro é {num} !')


def leiaFloat(msg):
    while True:
        try:
            n1 = int(input(msg))
        except (ValueError, TypeError):
            print("ERRO:Por favor, digite um número Real válido!")
            continue
        else:
            return n1

num1 = leiaFloat("Escreva um número Real: ")
print(f"O número real é {num1} !")

print(f"O valor inteiro foi {num} e o valor Real foi {num1} !")



