import random
import termcolor 
N = 30
t = 0
lf = []
lista = []
di = 0.6
tq = 3
px = [0,0.2,0.4,0.6,0.8,1,1,1,1]

if N <= 0:
        raise Exception("El numero de celdas debe ser positivo")

for i in range(N):  #Lista estado inicial
        lf=[]
        for i in range(N):         
                        lf.append(int(random.choices([-1, -2], [di, (1-di)])[0]))
        lista.append(lf)

alto = len(lista)                                      #Buscar centro e indendiarlo
ancho = len(lf)
if alto != ancho:
        raise Exception("Hubo un error inesperado")
elif alto % 2 == 0:  #Para matrices pares
        lista[int((alto/2))][int((ancho/2))]=tq
        lista[int((alto/2)-1)][int((ancho/2))]=tq
        lista[int((alto/2))][int((ancho/2)-1)]=tq
        lista[int((alto/2)-1)][int((ancho/2)-1)]=tq

        lista[int((alto/2+1))][int((ancho/2))]=tq
        lista[int((alto/2)+1)][int((ancho/2-1))]=tq
        lista[int((alto/2)+1)][int((ancho/2)+1)]=tq
        lista[int((alto/2))][int((ancho/2)+1)]=tq
        lista[int((alto/2)-1)][int((ancho/2)+1)]=tq

elif alto % 2 != 0: #Para matrices impares
        lista[int((alto/2))][int((ancho/2))]=tq
        lista[int((alto/2)-1)][int((ancho/2))]=tq
        lista[int((alto/2))][int((ancho/2)-1)]=tq
        lista[int((alto/2)-1)][int((ancho/2)-1)]=tq

        lista[int((alto/2+1))][int((ancho/2))]=tq
        lista[int((alto/2)+1)][int((ancho/2-1))]=tq
        lista[int((alto/2)+1)][int((ancho/2)+1)]=tq
        lista[int((alto/2))][int((ancho/2)+1)]=tq
        lista[int((alto/2)-1)][int((ancho/2)+1)]=tq

fuegosprendidos = 9 #Siempre empieza con 9 fuegos centrales 
def cant_fuegos (lista,fuegosprendidos):
        fuegosprendidos = 0
        for e in lista:
                for q in e:
                        if q > 0:
                                fuegosprendidos += 1
        return fuegosprendidos


while fuegosprendidos > 0: #Se va a ejecutar hasta que se termine de propagar el fuego 

        temporal = []
        for i in range(N):  #creo una matris similar a la base que la uso como temporal
                temporal1 = []
                for e in range(N):         
                                temporal1.append(int(-2))
                temporal.append(temporal1)


        for e1,fila in enumerate(lista): #enumerate para poder diferenciar entre los indices y los valores de la matriz (e1 es indice)
                for q1,valor_de_fila in enumerate(fila):
                        quemadosalrededor = 0 
                        if valor_de_fila == -2:
                                temporal[e1][q1] = -2
                        elif valor_de_fila == 3:
                                temporal[e1][q1] = 2
                        elif valor_de_fila == 2:
                                temporal[e1][q1] = 1
                        elif valor_de_fila == 1:
                                temporal[e1][q1] = 0
                        elif valor_de_fila == 0:
                                temporal[e1][q1] = 0
                        elif valor_de_fila < 0: 
                                for i in range(-1,2): #con estos ciclos de for recorro los cuadrantes alrededor de cada valor
                                        for j in range(-1,2):
                                                if i!=0 or j!=0:
                                                        vec_horizontal = e1 + i #son los casillas vecinas
                                                        vec_vertical = q1 + j
                                                        if (0 <= vec_horizontal < ancho) and (0 <= vec_vertical < alto): #compruebo que no este fuera de rango
                                                                valor_vec = lista[vec_horizontal][vec_vertical]
                                                                if valor_vec > 0: #si la casilla de alrededor esta incendiada lo almacena en una variable temporal
                                                                        quemadosalrededor = quemadosalrededor +1
                                if quemadosalrededor == 8: #luego de analizar los 8 casillas alrededor, segun la cant incendiada quema el valor con la prob px 
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[8],px[8]])[0]) #Lo almacena en la matriz temporal 
                                if quemadosalrededor == 7:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[7],px[7]])[0]) #Asi puede escanear toda la matriz inicial y dps cambiar valores
                                if quemadosalrededor == 6:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[6],px[6]])[0])
                                if quemadosalrededor == 5:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[5],px[5]])[0])
                                if quemadosalrededor == 4:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[4],px[4]])[0])
                                if quemadosalrededor == 3:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[3],px[3]])[0])
                                if quemadosalrededor == 2:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[2],px[2]])[0])
                                if quemadosalrededor == 1:
                                        temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[1],px[1]])[0])
                                if quemadosalrededor == 0:
                                        temporal[e1][q1] = lista[e1][q1] 
                    
                              
        for e,fila in enumerate(lista):  #Reemplaza los valores de la matriz temporal por mi matriz base
                for q,valor_de_fila in enumerate(fila):
                        lista[e][q] = temporal[e][q]

        for e in lista:    #Imprime la matriz 
                for q in e:
                        if q > 0:
                                print(termcolor.colored("▓▓","red"),end="")
                        if q ==-2:
                                print("  ", end="")
                        elif q ==-1:
                                print(termcolor.colored("▓▓","green"), end="")
                        elif q == 0:
                                print(termcolor.colored("▓▓","white"), end="")
                print("")        
                    

        quemados = 0
        vivos = 0
        prendidos = 0
        for e1 in lista:
                for q1 in e1:
                        if q1 == 0:
                                quemados = quemados + 1
                        elif q1 == -1:
                                vivos = vivos + 1
                        elif q1 > 0:
                                prendidos = prendidos +1

        print (termcolor.colored("Prendidos:","red"), termcolor.colored(prendidos,"red"))
        print(termcolor.colored("Vivos:","green"),termcolor.colored(vivos,"green"))
        print("Quemados:",quemados)

        fuegosprendidos = cant_fuegos(lista,fuegosprendidos)

        