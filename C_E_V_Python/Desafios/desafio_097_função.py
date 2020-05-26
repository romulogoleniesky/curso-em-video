#DESAFIO - 096(função):
#Realizar um programa que calcule a área de um terreno em
#metros quadrados.



#Definição da função:
def área(L, C):
    a = L * C
    print(f'O terreno com dimensões de {L} X {C}, tem área de {a} m²!')


#Programa principal:
print("Controle de Terrenos")
lar = float(input("Largura(m):"))
comp = float(input("Comprimento(m):"))

área(lar, comp)
