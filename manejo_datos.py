
x = """
EJEMPLO DE MANEJO DE ADATOS EN PYTHON 

"""

print(x)

#1 manejo de una lista 

lista = [1,2,3,4,5]
print(lista)
print()

lista.append(6) # agrega a la lista con el metodo append
print(lista)
print()

lista.remove(1) # se elimina de la lista con el metodo remove
print(lista)
print()


lista = [4,5,2,3,1]
print(f"lista sin ordenar, {lista}")
lista.sort() #ordana la lista normalmente de menor a mayor 
print(f"lista ordenara, {lista}")


#3 ALGORTIMO BURBUJA 
x = """
ALGORITMO BURBUJA PARA
ORDENAR UNA LISTA DE MENOR A MAYOR

"""
print()
print(x)

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista



numeros = [21,21,2,5,3,6]
print(f"NUMEROS SIN ORDENAR, {numeros}")
print()
print(f"NUMEROS ORDENADOS, {burbuja(numeros)}")

#4 MANEJO DE TUPLAS 
tupla = (1,2,3,4,5,"hola")
print(tupla)
print()

print(f"El primer elemento de la tupla es: {tupla[0]}")
print(f"La tupla tiene una longitud de {len(tupla)}")

#Diccionarios

print()
diccionario = {"nombre": "Juan","edad": 18, "ubicación": "Medellin"}
print(diccionario)
diccionario["edad"] = 20 # se cambia el valor de la clave edad
print(diccionario)
print(diccionario["ubicación"])
print()

# 5 TEORIA DE CONJUNTOS
x = """
TEORIA DE CONJUTNOS 
"""

print(x)
print()

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a)
print(b)

print("Union " , a | b )
print("Intersección " , a & b )
print("diferencia a-b" , a - b )
print("diferencia b-a" , b - a )
print()

# 6. Manejo de una matriz (lista de listas)
x = """
MANEJO DE UNA MATRIZ
"""

print(x)
print()

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matriz)

print("Elemento en (1,1):", matriz[1][1])
print("Matriz completa:")
for fila in matriz:
    print(fila)
