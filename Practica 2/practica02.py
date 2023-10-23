import random
import time
import matplotlib.pyplot as plt

#Funcion para crear arreglos aleatorios
def arregloAleatorio():
    #Creamos una lista para guardar los tiempos
    tiempos = []
    #Creamos una lista para guardar los tamaños
    tamaños = []
    #Creamos una lista para seguir los arreglos
    arreglos = []
    for _ in range(0,100):  # Realizar 100 experimentos
        # Creamos Arreglos aleatorios
        arreglo = [random.randint(0, 100) for i in range(random.randint(1, 100))]
        tamaños.append(len(arreglo))
        arreglos.append(arreglo)                       

        # Iniciamos a medir el tiempo
        inicio = time.time()
        quicksort(arreglo)
        fin = time.time()
        tiempo_ejecutado = fin - inicio
        tiempos.append(tiempo_ejecutado)

    # Ordenamos los tamaños y tiempos en función de los tamaños
    tamaños, tiempos, arreglos = zip(*sorted(zip(tamaños, tiempos, arreglos)))

    # Graficamos después de haber recopilado los datos
    plt.plot(tamaños, tiempos, marker='o', linestyle='-')
    plt.title("Quicksort")
    plt.xlabel("Tamaño del arreglo")
    plt.ylabel("Tiempo en ejecución (segundos)")
    plt.grid(True)
    plt.show()

    # Mostrar los 3 casos con menor tiempo
    print("Casos con menor tiempo de ejecución:")
    for i in range(3):
        print(f'Tamaño: {tamaños[i]}, Tiempo: {tiempos[i]}')
        print(f'Arreglo desordenado: {arreglos[i]}')
        print(f'Arreglo ordenado: {quicksort(arreglos[i])}\n')

    # Mostrar los 3 casos con mayor tiempo
    print("Casos con mayor tiempo de ejecución:")
    for i in range(-1, -4, -1):
        print(f'Tamaño: {tamaños[i]}, Tiempo: {tiempos[i]}')
        print(f'Arreglo desordenado: {arreglos[i]}')
        print(f'Arreglo ordenado: {quicksort(arreglos[i])}\n')
    

#Quicksort
#Funcion Quicksort
def quicksort(arreglo):
    #Cuando el arreglo solo tiene un valor estamos en el caso base
    if len(arreglo)<2:
        #Nos regresa la lista ordenada
        return arreglo
    
    izq, pivote, der = particion(arreglo)
    #Nos ordena el lado izquierdo y derecho tambien
    return quicksort(izq) + [pivote] + quicksort(der) 

#Funcion Auxiliar 
def particion(arreglo):
    #Creamos un pivote que sea igualado a 0
    pivote = arreglo[0]
    #Lista auxiliar para numeros menores
    izq = []
    #Lista auxiliar para numeros mayores
    der = []
    #Ciclo para separar los numeroes en mayores o menores, respecto al pivote
    for i in range(1, len(arreglo)):
        if arreglo[i]<pivote:
            izq.append(arreglo[i])
        else :
            der.append(arreglo[i])
    return izq, pivote, der

#print(quicksort(arreglo))

#Metodo para ejecutar el programa
if __name__ == '__main__' :
    arregloAleatorio()