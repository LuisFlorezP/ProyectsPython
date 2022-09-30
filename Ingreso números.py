#INGRESO NÚMEROS


print()
listaNumeros=[]
contador=0
while contador<5:
    print('Ingresa un número entre 5 y 10: ',end='')
    numero=int(input())
    if  numero>=5 and numero<=10:
        listaNumeros.append(numero)
    contador=contador+1
    break

print('\nLa lista de valores entre 5 y 10 ingresados es: ',listaNumeros,'\n')
