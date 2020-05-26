#DESAFIO - 097(função):
#Faça um programa que tenha uma função escreva(), que receba um texto
# e mostre ele com as linhas adaptadas ao seu tamanho.



#Definição da função:
def escreva(msg):
    tam = len(msg)+2
    print('~'*tam)
    print(f' {msg}')
    print('~'*tam)


def escreva1(msg1):
    tam1 = len(msg1)+2
    print('~'*tam1)
    print(f' {msg1}')
    print('~'*tam1)



#Programa principal:
print("Você escreverá duas mensagens de tamanhos diferentes e veja como as linhas se adaptam às mensagens!")
texto = str(input("Escreva aqui a primeira mensagem: "))
texto1 = str(input("Agora, escreva aqui a segunda mensagem: "))
escreva(texto)
escreva1(texto1)
