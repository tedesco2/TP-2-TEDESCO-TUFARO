import random
import termcolor 

#IMPORTO MIS FUNCIONES 
from TP1_FUNCIONES_TUFARO import*

#DEFINO VARIABLES
N = 30
di = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
tq = 3
px = [0,0.2,0.4,0.6,0.8,1,1,1,1]
porcentajes_de_quemados = [] #la lista donde se van a almacenar los porcentajes quemados para cada densidad

#COMIENZO LAS SIMULACIONES POR DENSIDAD
for dens in di:
        simulaciones = 0 
        list_temp_porcentajes = [] #Una lista temporal para almacenar los porcentajes de cada simulacion de 1 densidad
        while simulaciones < 100:
                simulaciones += 1       #Contador de simulaciones
                lista = []              #Defino mi lista/matriz inicial
                fuegosprendidos = 0     #Defino mi contador de fuegos

                lista = crear_bosque(N,lista,dens) #Creo la matriz general del bosque (lista)
                arboles_vivos_iniciales = cant_arb_vivos(lista) #Cuenta los arboles vivos que habia al inicio de la simulacion
                quemar_centro(lista,tq) #Busca el centro y lo incendia   
                fuegosprendidos =  cant_fuegos(lista,fuegosprendidos)#Siempre empieza con 9 fuegos centrales 

                while fuegosprendidos > 0: #Comienza el ciclo de propagacion hasta que termine el incencencio (no haya arboles prendidos)
                        temporal = crear_matriz_temporal(N) #creo una matris similar a la base que la uso como temporal. Asi puede escanear toda la matriz inicial y dps cambiar valores
                        propagacion_fuego(lista,N,px,tq,temporal) #Ejecuta la funcion que propaga el fuego                                             

                        fuegosprendidos = cant_fuegos(lista,fuegosprendidos) #Cuando esta variable es 0 el bucle se detiene

                arboles_quemados = cant_arb_quemados(lista) #Cuenta la cantidad de arboles quemados en la simulacion
                porc_quemados = densidad_arb_quemados(arboles_quemados,arboles_vivos_iniciales) #Saca el promedio de quemados por simulacion
                list_temp_porcentajes += [porc_quemados] #Guarda ese porcentaje en la lista temporal de porcentajes

        promedio_por_densidad = prom_por_densidad(list_temp_porcentajes,simulaciones) #Saco el promedio de quemados por cada densidad
        porcentajes_de_quemados += [promedio_por_densidad] #Lo almaceno en la lista principal y comienza una nueva simulacion por otra densidad

#IMPRIMO LA TABLA     
renglon = f"+----------+----------------+" #creo f-strings para evitar repeciones de print
titulo = f"| Densidad | Bosque quemado |"
print(renglon)
print(titulo)
for i in range(10): #Automatizo la impresion de la tabla 
        print(renglon)
        densidad = di[i] 
        porcentaje = porcentajes_de_quemados[i]
        cant_digitos = len(str(porcentaje)) #Para poder diferenciar entre los valores de 2 cifras y 1, y con 2 o 1 decimal
        if cant_digitos == 3: #La diferenciacion la hago para que siempre queden centrados en la tabla (el "." lo cuenta como un digito)
                linea_texto = f"| {densidad}      |   {porcentaje} %        |"
        if cant_digitos == 4: 
                linea_texto = f"| {densidad}      |   {porcentaje} %       |"
        elif cant_digitos == 5: 
                linea_texto = f"| {densidad}      |  {porcentaje} %       |"
        elif cant_digitos == 6:
                linea_texto = f"| {densidad}      | {porcentaje} %       |"
        print(linea_texto)
print(renglon)

    
                    
            