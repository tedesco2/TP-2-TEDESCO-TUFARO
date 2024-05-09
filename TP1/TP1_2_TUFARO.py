import random
import termcolor 

#IMPORTO MIS FUNCIONES 
from TP1_FUNCIONES_TUFARO import*

#DEFINO VARIABLES
N = 30          #Tamaño de la matriz
di = 0.6        #Densidad del bosque       
tq = 3          #Estado inicial de fuego
temporal = []   #matriz para almacenar temporalmente valores
tiempos = []    #Lista donde se acumulan los tiempos finales de cada simulacion
simulaciones = 0 #Contador de simulaciones
fuegosprendidos = 0 #Variable que almacena la cantidad de arboles encendidos
px = [0,0.2,0.4,0.6,0.8,1,1,1,1] 
assert N > 0, "El parametro N debe ser positivo"

#COMIENZAN LAS SIMULACIONES
while simulaciones < 1000: #Creo el bucle para ejecutar las 1000 simulaciones
        simulaciones +=1 #contador de simulaciones
        contador = 0 #Reinicio el contador de simulaciones en el arranque de cada una
        lista =[] #Reincio la lista en cada simulacion
        crear_bosque(N,lista,di)
        quemar_centro(lista,tq)
        fuegosprendidos = cant_fuegos(lista,fuegosprendidos) #Siempre empieza con 9 fuegos centrales
        
        while fuegosprendidos > 0: #Se va a ejecutar hasta que se termine de propagar el fuego 
                temporal = crear_matriz_temporal(N)
                propagacion_fuego(lista,N,px,tq,temporal)                                         

                fuegosprendidos = cant_fuegos(lista,fuegosprendidos) #Cuando esta variable es 0 el bucle se detiene
                contador += 1 #cuanta la cantidad de tiempos que tarda cada simulacion en terminar de propagarse
        tiempos += [contador] #Guarda la cantidad de tiempos que tardo en la lista de tiempos

promedio = promedio_simulaciones(tiempos,simulaciones) #Obtengo el promedio de tiempo de incendio

print("El tiempo promedio que tarda un incendio en extiguirse naturalmente es: ",promedio,"minutos")