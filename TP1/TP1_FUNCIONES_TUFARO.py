import random
import termcolor

#DEFINO TODAS LAS FUNCIONES QUE USE PARA EL TP1
def crear_bosque(N,lista,di):
    #Crea la matriz inicial que la entendemos como bosque
    for e in range(N):
            lf=[]
            for q in range(N):
                val_aleatorio = random.random() #Crea un valor aleatorio entre 0 y 1(inclusive)
                if val_aleatorio <= di: #Hay un 60% de chances de que el valor aleatorio sea menor que 0.6 
                    lf += [-1] #Si esto ocurre se crea un arbol
                else:
                    lf += [-2] #Sino se crea un espacio vacio
            lista += [lf]
    return lista
def crear_matriz_temporal (N):
        #Crea una matriz igual que el bosque (30x30) que la utilizo para almacenar valores temporalmente
        temp1 = [] 
        for i in range(N):  
                temp2 = []
                for e in range(N):         
                                temp2 += [int(-2)]  
                temp1 += [temp2]
        return temp1
def imprimir_matriz (lista):
         #Imprime la matriz con colores segun cada valor
         for e in lista:    
                for q in e: #Escanea todos los valores de la matriz y los imprime segun su valor
                        if q > 0:
                                print(termcolor.colored("▓▓","red"),end="") 
                        if q ==-2:
                                print("  ", end="")
                        elif q ==-1:
                                print(termcolor.colored("▓▓","green"), end="")
                        elif q == 0:
                                print(termcolor.colored("▓▓","white"), end="")
                print("") #Crea un nuevo renglon cada vez que termina una lista, que equivale a una fila
def quemar_centro(lista,tq): 
    #Busca el centro de la matriz y lo incendia, osea lo iguala a tq
    alto = len(lista) #Si bien es un tanto redundante definir el alto y el ancho por separado
    ancho = len(lista) #Me resulta mas comodo para interpretar bien cuando actua cada uno, Por eso los defini asi
    if alto != ancho: #si no son iguales la matriz no es cuadrada
            raise Exception("hubo un error inesperado en la matriz")
    else: #Como siempre el centor es de 3x3 por mas que sea par o impar hay que pintar las casillas centrales
            lista[int((alto/2))][int((ancho/2))]=tq
            lista[int((alto/2)-1)][int((ancho/2))]=tq
            lista[int((alto/2))][int((ancho/2)-1)]=tq
            lista[int((alto/2)-1)][int((ancho/2)-1)]=tq

            lista[int((alto/2+1))][int((ancho/2))]=tq
            lista[int((alto/2)+1)][int((ancho/2-1))]=tq
            lista[int((alto/2)+1)][int((ancho/2)+1)]=tq
            lista[int((alto/2))][int((ancho/2)+1)]=tq
            lista[int((alto/2)-1)][int((ancho/2)+1)]=tq
def quemar_arboles_aleatoriamente (quemadosalrededor,lista,temporal,px,tq,e1,q1):
        #Esta funcion es la que transforma "aleatoriamente" los arboles vivos a prendidos fuego segun la cant de vecinos encendidos
        if quemadosalrededor != 0: #luego de analizar los 8 casillas alrededor, segun la cant incendiada quema el valor con la prob px
                    r = random.random() # Genera un valor aleatorio entre 0 y 1
                    if r <= px[quemadosalrededor]: #si la probabilidad asignada segun la cant de arboles quemados es mayor que el num aleatorio
                        temporal[e1][q1] = tq #Incendia la casilla
                    else:
                        temporal[e1][q1] = lista[e1][q1] #Sino deja el valor que estaba
        else: #si no hay vecinos quemandose, deja el valor que estaba porque no hay posibilidad de incendio
                temporal[e1][q1] = lista[e1][q1] 
def quemar_arboles_aleatoriamente_alternativa(quemadosalrededor,lista,temporal,px,tq,e1,q1):
        """
        Esta fue mi primer alternativa para elegir aleatoriamente si quemar la casilla o no
        Use el random choices porque es la funcion que me parecia mas intuitiva ya que,
        como tenia que elegir entre dos valores, que eran conserval su prenderlo fuego (tq),
        con el random.choices podia elgir entre estos dos valores asignandole una probabilidad "aleatoria"
        a que salgan elegidos. Funciono tal como deberia pero como la idea era usar random.random lo modifique :D
        """
        if quemadosalrededor != 0: #luego de analizar los 8 casillas alrededor, segun la cant incendiada quema el valor con la prob px
                temporal[e1][q1] = int(random.choices([lista[e1][q1], tq], [1-px[quemadosalrededor],px[quemadosalrededor]])[0]) #Lo almacena en la matriz temporal 
        if quemadosalrededor == 0:
                temporal[e1][q1] = lista[e1][q1]
def contador_estados (lista):
        #cuento la cantidad de quemados, vivos y prendidos que hay en la matriz para llevar el registro
        quemados = 0
        vivos = 0
        prendidos = 0
        for e1 in lista: #Recorre los valores de la matriz y los analiza
                for q1 in e1:
                        if q1 == 0:
                                quemados += 1
                        elif q1 == -1:
                                vivos += 1
                        elif q1 > 0:
                                prendidos += 1
        return quemados, vivos, prendidos    
def propagacion_fuego (lista,N,px,tq,temporal):
        """
        Esta funcion se encarga de analizar cada valor de la matriz original (lista) y segun lo que encuentre lo almacena
        en una matriz temporal (temporal). Si encuentra vacio, deja vacio. Si encuentra fuego, resta uno para ir apagando el fuego.
        Si encuentra un arbol quemado, deja el arbol quemado. Y si encuentra un arbol vivo, cuenta cuantos vecinos alrededor
        estan prendidos fuego y los quema con una probablidad aleatoria que depende de esa cantidad.
        Finalmente obtenemos una matriz temporal con todos los valores actualizados del bosque, que luego se copian a la matriz original
        """
        alto = len(lista) #Si bien es un tanto redundante definir el alto y el ancho por separado
        ancho = len(lista) #Me resulta mas comodo para interpretar bien cuando actua cada uno, Por eso los defini asi
        for e1 in range(N): #Creo dos for consecutivos en rango N que me van a recorrer la variable horizontal y verticalmente
                for q1 in range(N): #q1 va a ser el valor de columna y e1 el valor de fila
                        quemadosalrededor = 0 #Defino una variable para saber los quemados alrededor de cada casilla
                        if lista[e1][q1] == -2: #Si el valor es -2 queda igual
                                temporal[e1][q1] = -2
                        elif lista[e1][q1] == 3:  #Si la casilla esta prendida, se le resta 1 
                                temporal[e1][q1] = 2
                        elif lista[e1][q1] == 2:
                                temporal[e1][q1] = 1
                        elif lista[e1][q1] == 1:
                                temporal[e1][q1] = 0 
                        elif lista[e1][q1] == 0: #Si la casilla estaba prendida y se apago queda apagada en 0 
                                temporal[e1][q1] = 0
                        elif lista[e1][q1] < 0: #si la casilla tiene un arbol vivo, hay que analizar si debe incendiarse o no
                                for i in range(-1,2): #con estos ciclos de for recorro los cuadrantes alrededor de cada valor
                                        for j in range(-1,2): 
                                                if i!=0 or j!=0: #evita que analice si la casilla propia (i=0, j=0) esta en fuego, lo que no tendria sentido
                                                        vec_horizontal = e1 + i #son los casillas vecinas
                                                        vec_vertical = q1 + j 
                                                        if (0 <= vec_horizontal < ancho) and (0 <= vec_vertical < alto): #compruebo que no este fuera de rango
                                                                valor_vec = lista[vec_horizontal][vec_vertical] #creo una variable que le asigno el valor de la matriz en ese punto
                                                                if valor_vec > 0: #si la casilla de alrededor esta incendiada lo almacena en una variable temporal
                                                                        quemadosalrededor = quemadosalrededor +1 
                                quemar_arboles_aleatoriamente (quemadosalrededor,lista,temporal,px,tq,e1,q1)
        for e in range(N):  #Reemplaza los valores de la matriz temporal por mi matriz base
                for q in range(N):
                        lista[e][q] = temporal[e][q]
def promedio_simulaciones(tiempos,simulaciones):
        #A partir de todos los tiempos de inencdio calcula un promedio de todas las simulaciones
        tiempo_total = 0 
        for e in tiempos:
                tiempo_total += e #suma todos los tiempos que tardo cada simulacion
        prom = round(tiempo_total/simulaciones,2) #Divide el tiempo total por la cant de simulaciones para sacar el promedio
        return prom
def cant_arb_vivos (lista): 
        #Escanea la matriz y cuenta los arboles vivos
        arboles_vivos = 0
        for e in lista:
                for q in e:
                        if q == -1:
                                arboles_vivos += 1
        return arboles_vivos
def cant_arb_quemados (lista): 
        #Escanea la matriz y cuenta los arboles que se quemaron (ya apagados)
        arboles_quemados = 0
        for e in lista:
                for q in e:
                        if q == 0:
                                arboles_quemados += 1
        return arboles_quemados
def cant_fuegos (lista,fuegosprendidos):
        fuegosprendidos = 0
        for e in lista:
                for q in e:
                        if q > 0:
                                fuegosprendidos += 1
        return fuegosprendidos
def densidad_arb_quemados (arboles_quemados,arboles_vivos_iniciales): 
        #Nos da el valor en porcentaje de la cantidad de arboles que se quemaron en la simulacion
        densquemados = round((arboles_quemados/arboles_vivos_iniciales)*100, 2)
        return densquemados
def prom_por_densidad(list_temp_porcentajes,simulaciones):
        suma_porcentajes = 0
        for e in list_temp_porcentajes:
                suma_porcentajes += e
        promedio_por_densidad = round(suma_porcentajes/simulaciones,2)
        return promedio_por_densidad
