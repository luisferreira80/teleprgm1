#!/usr/bin/python3
# esto es un comentario.

# esto es una funcion
def ImprimeLimitador():
    print("+---------------------------------------------------------------+")


vEdadPromedio = 30
if vEdadPromedio >= 21:
    print("su edad es correcta para entrar a este lugar")

# # lista
ImprimeLimitador()
vPrimeraLista = ["f", "1", ["a", "b"], "casa"]
# elementos de la lista
print("elemento 1 de mi lista: ", vPrimeraLista[1])
print("elemento 1 del segundo elemento de mi lista: ", vPrimeraLista[2][1])


# # Declaracion de una tupla:
ImprimeLimitador()
vPrimeraTupla = (1, "abc", True)
print("Estoy imprimiendo la primera tupla: ", vPrimeraTupla)
# acceso a valores
print("Este es el primer elemento de vPrimeraTupla: ", vPrimeraTupla[0])
print("Este es el -1 elemento de vPrimeraTupla: ", vPrimeraTupla[-1])

# # Entrada de datos, conversion de tipos e impresion en pantalla

vEntrada = input("introduzca un número: ")
# CONDICIONALES
# if
vClave = int(vEntrada)

if vClave >= 25:
    print("vClave es mayor o igual a 25")
    print("se evaluo el primer if")
elif vClave < 10:
    print("el valor de vClave en menor a 10")
else:
    print("el valor de vClave esta entre 10 y 25")

for vElementoEnVentrada in vEntrada:
    print("el recorrido va en:", vElementoEnVentrada)
