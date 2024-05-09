import random
import termcolor 

#iMPORTO MIS FUNCIONES 
from TP1_FUNCIONES_TUFARO import*

#DEFINO VARIABLES                            
N = 30          #Tamaño de la matriz
lista = []      #lista donde voy a guardar mi matriz/bosque
di = 0.6        #Densidad del bosque       
tq = 3          #Estado inicial de fuego
temporal = []   #Matriz similar a lista para alamecenamiento temporal de datos
px = [0,0.2,0.4,0.6,0.8,1,1,1,1] #Probablidades de incendio segun cant de vecinos incendiados  
fuegosprendidos = 0 #Variable que almacena la cantidad de arboles encendidos
assert N > 0, "El parametro N debe ser positivo" #En caso de que se modifique el valor de N y se introduzca un valor no apto

#COMIENZO DEL PROGRAMA

lista = crear_bosque(N,lista,di) #Creo la matriz general del bosque (lista)
quemar_centro(lista,tq) #Busca el centro y lo incendia
imprimir_matriz(lista) #Imprime la matriz en su estado inicial      
fuegosprendidos =  cant_fuegos(lista,fuegosprendidos)#Siempre empieza con 9 fuegos centrales 

while fuegosprendidos > 0: #Comienza el ciclo de propagacion hasta que termine el incencencio (no haya arboles prendidos)
        temporal = crear_matriz_temporal(N) #creo una matris similar a la base que la uso como temporal. Asi puede escanear toda la matriz inicial y dps cambiar valores
        propagacion_fuego(lista,N,px,tq,temporal) #Ejecuta la funcion que propaga el fuego                                             
        imprimir_matriz(lista) #Imprimo la matriz  

        quemados, vivos, prendidos = contador_estados (lista) #Cuento los estados de toda mi matriz 
        #Imprimo los estados de la matriz
        print (termcolor.colored("Prendidos:","red"), termcolor.colored(prendidos,"red")) 
        print(termcolor.colored("Vivos:","green"),termcolor.colored(vivos,"green"))
        print("Quemados:",quemados)
        fuegosprendidos = prendidos     #Cuando esta variable es 0 el bucle se detiene y termina el programa
