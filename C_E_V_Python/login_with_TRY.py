import getpass

print("----"*10)
print("Cadastre uma senha de 4 digitos:")
a = int(input("           Senha : "))
b = getpass.getpass("Confirme a Senha : ")
s = a == b

if ( s == True):
    print("Senha Cadastrada, agora faça o Login!");
else:
    print("Senha diferente!")
