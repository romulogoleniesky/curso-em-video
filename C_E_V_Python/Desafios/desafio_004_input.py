# DESAFIO - 004 - INPUT - AULA 06:
# Faça um programa que receba uma informação e mostre na tela as caracteristicas dela.

dado = input("Digite algo: ")
print("Qual o tipo primitivo? ", type(dado))
print("Só tem espaço? ", dado.isspace())
print("É um número?", dado.isnumeric())
print("É alfabetico?", dado.isalpha())
print("É alfanumerico? ", dado.isalnum())
print("Está em letra Maiuscula?", dado.isupper())
print("Está em letra minuscula?", dado.islower())
print("Está capitalizado?", dado.istitle())

#FIM

