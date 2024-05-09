# -*- coding: utf-8 -*-
"""
Repaso Parcial - I100  (2024a)

# Slicing
"""

# Slicing completo
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
lista = L[:]
print(lista)

# Slicing completo en reversa
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
print(L[::-1])

# Slicing desde un íncice dado hasta el final
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
print(L[4:])  # Entre 4 y el último

# Slicing desde el inicio hasta un índice dado
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
print(L[:6])  # Entre 0 y 5 (no se incluye el 6)
print(L[0:6]) # Entre 0 y 5 (no se incluye el 6)

# Slicing en un rango dado de elementos
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
print(L[3:8]) # Entre 3 y 7 (no se incluye el 8)

# Slicing salteando elementos
L = [1, 4, 8, 3, 5, 0, 10, 4, 6, 7, -2]
print(L[0::3]) # Entre 0 y el último en pasos de 3
print(L[::3])  # Entre 0 y el último en pasos de 3

"""# Enumerate"""

# Iterar sobre un string sin usar enumerate
pal = 'palabra'
for i in range(len(pal)):
  print(f'caracter {i+1}: {pal[i]}')

# Iterar sobre un string usando enumerate
for i,c in enumerate('palabra', 1):
  print(f'caracter {i}: {c}')

# Ejemplos de enumerate
lista = ['Argentina','Brasil','Polonia','Australia']
for i, pais in enumerate(lista):
  print(f'pais {i}: {pais}')

# Ejemplos de enumerate
dic = {'Argentina':'America',
       'Brasil':'America',
       'Polonia': 'Europa',
       'Australia':'Oceania'}

for i, (pais, continente) in enumerate(dic.items(), 1):
  print(f'{i}. Pais: {pais}, Continente: {continente}')

"""# Función ZIP"""

# uso de la función zip()

lista1 = ['rojo', 'verde', 'azul', 'blanco', 'negro']
lista2 = [0.5, 0.1, 0.8, 0.75, 0.0]
lista3 = list(zip(lista1, lista2))

print(lista3)

for l1, l2 in zip(lista1, lista2):
  print(l1, l2)

"""# Mutabilidad y Aliasing"""

# Función que modifica la lista de números

def elevar_al_cuadrado(lista):
    for i, e in enumerate(lista):
        lista[i] = e ** 2

lista_vieja = list(range(10))
print('lista_vieja:', lista_vieja)

elevar_al_cuadrado(lista_vieja)
print('lista vieja:', lista_vieja)

# Notar que los cambios en dentro de la función lista_vieja() se reflejan afuera
# (como la variable es solo una referencia, al ser mutable los cambios se mantienen)

# Función que retorna una lista sin modificar la original

def elevar_al_cuadrado(lista_de_numeros):
    lista = lista_de_numeros[:] # hacemos una copia (tambíén cpuede usarse .copy())
    for i,e in enumerate(lista):
        lista[i] = e ** 2
    return lista

lista_vieja = list(range(10))
print('lista_vieja:', lista_vieja)

lista_nueva = elevar_al_cuadrado(lista_vieja)
print('lista nueva:', lista_nueva)
print('lista vieja:', lista_vieja)

# Al hacer una copia de la lista y no se modifica la original

# Función que modifica un diccionario (pone en 0 todos los valor)

def resetear_dic(d):
    dic = d
    for k in dic.keys():
        dic[k] = 0
    return dic # se moifica d?

lista1 = ['rojo','verde', 'azul', 'blanco', 'negro']
lista2 = [0.5, 0.1, 0.8, 0.75, 0.0]
dic_viejo = dict(zip(lista1,lista2))

print('diccionario viejo:', dic_viejo)
dic_nuevo = resetear_dic(dic_viejo)
print('diccionario nuevo:', dic_nuevo)
print('diccionario viejo:', dic_viejo)

"""# Listas y diciconarios de comprensión"""

# Crear un vector de ceros (lista con elementos en 0 [0, 0, 0,...])
n = int(input("Ingrese el largo del vector: "))
vector_nulo = [0 for _ in range(n)]
print(vector_nulo)

# Crear un vector con valores aleatorios (entre 0 y 50)
import random
n = int(input("Ingrese el largo del vector: "))
vector_rand = [random.randint(0,50) for _ in range(n)]
print(vector_rand)

# Crear un diccionario a partir de dos listas usando diccionarios de comprensión
lista1 = ['rojo','verde', 'azul', 'blanco', 'negro']
lista2 = [0.5, 0.1, 0.8, 0.75, 0.0]
dicc = {clave:valor for clave, valor in zip(lista1, lista2)}
dic2 = dict(zip(lista1,lista2))
print(dicc,"\n",dic2)

"""# Métodos sobre Cadenas

split()
"""

# Ejemplo 1
print('\nEjemplo 1')
cadena = "Hola a todos, estamos en el campus Victoria!"
lista_str = cadena.split()
print(lista_str)

# Ejemplo 2
print('\nEjemplo 2')
sumas = "2+5+3+1+4+9"
lista = sumas.split("+")
suma = 0
for s in lista:
  suma += float(s)
suma2 = sum(float(e) for e in lista)
print(lista)
print(suma2)

# Ejemplo 3
print('\nEjemplo 3')
HHMMSS = "14:31:06"
time_units = HHMMSS.split(":")
horas = time_units[0]
min = time_units[1]
seg = time_units[2]
print(f'Son las {horas} horas, {min} minutos, {seg} segundos.')

"""join()"""

# Ejemplo 1 (directorios)
print('\nEjemplo 1')
directorios = ['C:', 'Users', 'Ana', 'Desktop', 'PC', 'Clase_16']
ruta = "/".join(directorios)
print(ruta)

# Ejemplo 2 (quitar caracteres no deseados de una cadena)
print('\nEjemplo 2')
cadena = "Hola, qué hora es? A qué hora comemos? Qué van a tomar el viernes?"

lista_aux = cadena.split(",")
cadena_aux = "".join(lista_aux)
print('\n',lista_aux)
print(cadena_aux)

lista_aux = cadena_aux.split("?")
cadena_aux = "".join(lista_aux)
print('\n',lista_aux)
print(cadena_aux.lower())

"""lower() y upper()"""

# Ejemplo 1.A
palabra_clave = "udesa2024"

p = input("Ingrese la palabra clave: ")
if p.lower() == palabra_clave:
  print("Palabra correcta!")
else:
  print("Inténtelo más tarde")

# Ejemplo 1.B
palabra_clave = "UDESA2024"

p = input("Ingrese la palabra clave: ")
if p.upper() == palabra_clave:
  print("Palabra correcta!")
else:
  print("Inténtelo más tarde")

"""isdecimal()"""

# Ingresar un entero positivo y chequear que sea decimal

str_entero = input('Ingrese un entero positivo: ')
while not(str_entero.isdecimal()):
  str_entero = input('Error: debe ingresar un entero positivo:')

int_entero = int(str_entero)
print(int_entero)

# Chequear que elementos de una secuencia sean digitos decimales
sumas = "2+5+3+1+AA+9"
lista = sumas.split("+")
suma = 0
for s in lista:
  if not s.isdecimal():
    print('La suma no es válida. Elemento no numérico.')
    suma = 0
    break
  suma += float(s)

print(lista)
print(suma)

"""find()"""

# Hallar posición de una cadena dentro de otra

# Ejemplo 1
directorio = "C:/Users/Ana/Desktop/PC/Clase_16"
i = directorio.find("Desktop")
print(directorio[0:i])

# Ejemplo 2
i = directorio.find("Documents")
if i==-1:
  print('Ruta no encontrada')
else:
  print(directorio[0:i])

"""# Métodos sobre listas

index()
"""

# Buscar primer elemento que concide
L = [12, 21, 26, 3, 15, 42, 9, 28, 42, 0, 1, 42, 48]
i = L.index(42)
print(i, L[i])

# El segundo parametro, index(valor, start), indica la posicion de inicio L[start:]
# Buscar siguiente elemento
i = L.index(42, i+1)
print(i, L[i])

# Buscar siguiente elemento
i = L.index(42, i+1)
print(i, L[i])

"""sort() vs sorted()"""

# sort(): es un METODO que "MODIFICA LA LISTA, NO RETORNA NADA"
L = [12, 21, 26, 3, 15, 42, 9, 28, 42, 0, 1, 42, 48]
L.sort() # ordena de menor a mayor por defecto
print(L)
L.sort(reverse=True) # el argumento reverse permite ordenar de mayor a menor
print(L)

# sorted(): es una FUNCIÓN que "NO MODIFICA LA LISTA, RETORNA OTRA LISTA"
L = [12, 21, 26, 3, 15, 42, 9, 28, 42, 0, 1, 42, 48]
L2 = sorted(L)
print(L)
print(L2)

# La diferencia entre ambas es que sort() es un método de listas, y sorted() una función

"""aplicar una función antes de ordenar"""

# sort tiene un argumento que permite aplicar una función antes de ordenar la secuencia
L = [12, -21, 26, -3, 15, -42, -9, 28, 42, 0, 1, -42, 48]
# defino una función lambda que aplica abs al elemento
apply_abs = lambda elemento : abs(elemento)
# la función lambda pasada como argumento 'key' y sort aplicará apply_abs antes de considerar cada elemento para su ordenamiento
L.sort(key=apply_abs)
print(L) # L se ordena considerando el módulo de los elementos

# más información en la documentación oficial de python:
#https://docs.python.org/3/howto/sorting.html

"""append()"""

# Añadir elementos a una lista

L = [1, 2, 3]
print(L)

L.append(5)
print(L)

L.append(0)
print(L)

L.append('Argentina')
print(L)

L.append([0, 3, 5])
print(L)

"""extend()"""

# Extender una lista con elementos de un iterable

L = [1, 2, 3]
print(L)

L.extend('Oso')
print(L)

L.extend([True, False])
print(L)

L.extend(range(4))
print(L)

"""# Métodos sobre diccionarios

keys()
"""

# Método para crear un iterable de claves
D = {'lunes':1, 'martes':2, 'miercoles':3, 'jueves': 4, 'viernes': 5}

print(D)              # diccionario
print(D.keys())       # iterable de clave
print(list(D.keys())) # iterable de clave casteado a lista
for k in D.keys():    # iterable de clave iterado en ciclo for
  print(k)

"""values()"""

# Método para crear un iterable de valores
D = {'lunes':1, 'martes':2, 'miercoles':3, 'jueves': 4, 'viernes': 5}
print(D)                # diccionario
print(D.values())       # iterable de valor
print(list(D.values())) # iterable de valor casteado a lista
for v in D.values():    # iterable de valor iterado en ciclo for
  print(v)

"""items()"""

# Método para crear un iterable de clave-valor

D = {'lunes':1, 'martes':2, 'miercoles':3, 'jueves': 4, 'viernes': 5}

print(D)                # diccionario
print(D.items())        # iterable de clave-valor
print(list(D.items()))  # iterable de clave-valor casteado a lista (de tuplas)
for k,v in D.items():   # iterable de clave-valor iterado en ciclo for
  print(k, v)

"""get()"""

# Leer el valor para una determinada clave (pero con opciones de default)

D = {'lunes':1, 'martes':2, 'miercoles':3, 'jueves': 4, 'viernes': 5}

print(D.get('martes'))                # Leer valor con clave existente
print(D.get('sábado'))                # Leer valor con clave inexistnete
print(D.get('sábado', 'No se sabe'))  # Leer valor con clave inexistnete y opción por defecto

"""# Type hints"""

# Ejemplo 1 (armar directorios). Definir typhints

print("\nEjemplo 1")
def list_to_path(lista_carpetas: list) -> str:
      return "/".join(directorios)

directorios = ['C:', 'Users', 'Ana', 'Desktop', 'PC', 'Clase_16']
ruta = list_to_path(directorios)
print(ruta)

# Ejemplo 2 (quitar caracteres no deseados de una cadena). Definir typhints

print("\nEjemplo 2")
def quitar_signos(cadena:str, signos:str) -> str:
   cadena_aux = cadena
   for s in signos:
      lista_aux = cadena_aux.split(s)
      cadena_aux = "".join(lista_aux)
   return cadena_aux

cadena = "Hola, qué hora es? A qué hora comemos? Qué van a tomar el viernes?"
cadena_new = quitar_signos(cadena, ",?")
print(cadena)
print(cadena_new)

# Ejemplo 3 (suma de números desde un string)

print('\nEjemplo 3')
def str_to_sum(cadena_sumas:str) -> float:
    lista = cadena_sumas.split("+")
    suma = 0
    for s in lista:
      if not (s.isdecimal()):
         print("Error")
         suma = 0
         break
      suma += float(s)
    return suma

sum = str_to_sum("2+5+3+1+4+9")
print(sum)

"""# Operaciones y tipos"""

import math

# multiplicación entre mismo tipo
num1 = 10 # entero
num2 = 2 # entero
print(f'{num1 * num2} {type(num1 * num2)}')

# multiplicación entre diferentes tipos
num1 = 10 # entero
num2 = 2.5 # float
print(f'{num1 * num2} {type(num1 * num2)}')

# resto entero
num1 = 10 # entero
num2 = 2 # float
print(f'{num1 % num2} {type(num1 % num2)}')

# resto con coma
num1 = 10 # entero
num2 = 2.5 # float
print(f'{num1 % num2} {type(num1 % num2)}')

# división entera (redondea hacia abajo siempre)
num1 = 3900
num2 = 2000
print(f'{num1 // num2} {type(num1 // num2)}')
print(f'{math.floor(num1 / num2)} {type(math.floor(num1 / num2))}') # es equivalente a utilizar la función math.floor