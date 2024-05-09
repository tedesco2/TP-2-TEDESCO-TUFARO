import random
import os
numeros = [1,2,3,4,5,6,7,8,9]
num_correcto = []
num_usuario = []
for i in range(4):
    num = random.choice(numeros)
    num_correcto += [num]

usuario = input('Introduce un numero de 4 cifras')

if len(usuario) != 4:
    raise ValueError("El numero tiene que ser de 4 cifras")
for i in usuario:
    num_usuario += [int(i)]


while num_correcto != num_usuario:
    print("")
    print("Tu numero ahora es:",*num_usuario)
    posicion = 0
    for i in range(4):
            posicion +=1
            if num_usuario[i] in num_correcto:
                if num_usuario[i] == num_correcto[i]:
                    print("El",posicion,"°","digito es correcto y esta en la posicion correcta")
                else:
                    print("El",posicion,"°","digito es correcto pero esta en la posiscion incorrecta")
            else:
                print("El",posicion,"°","digito no es correcto")

    usuario = input('Introduce un nuevo numero de 4 cifras')
    num_usuario = []
    if len(usuario) != 4:
        raise ValueError("El numero tiene que ser de 4 cifras")
    for i in usuario:
        num_usuario += [int(i)]
    os.system('cls')

print("Adivinaste! el numero era: ",*num_usuario)