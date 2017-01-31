#!-/usr/bin/python3

fich = open('/etc/passwd','r')
lista_lineas = fich.readlines()

for usuario in lista_lineas:
    lista_split = usuario.split(":")
    login = lista_split[0]
    shell = lista_split[-1][:-1]
    print ("user:",login,"=> shell:", shell)

print ("\nNumero de usuarios:", len(lista_lineas))

fich.close()
