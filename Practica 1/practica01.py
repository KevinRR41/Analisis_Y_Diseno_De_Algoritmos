#Programa menu de burbujas
import time #Libreria para el tiempo
import sys
inicio = time.time()

#Se declara el arreglo
arreglo = []

#Llenamos el arreglo
def llenarArreglo(arreglo):
    for i in range(0,5):
        arreglo.insert(i,int(input(f'Introduzca el dato No. {i+1} : ')))

#Imprimimos el arreglo
def imprimirArreglo(arreglo):
    print("Asi quedo el arreglo: ")
    for i in range(0,5):
        print(arreglo[i])
#Metodo de la burbuja
def metodoBurbuja(arreglo):
    print("Muy bien usted a escogido el metodo de burbuja")
    llenarArreglo(arreglo)
    imprimirArreglo(arreglo)
    for i in range(1,5):
         for j in range(0,5-i):
            if(arreglo[j]>arreglo[j+1]):
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
    print("Muy bien he acabado de ordenar el arreglo, y ha quedado asi:")
    imprimirArreglo(arreglo)

#Metodo de la burbuja mejorado
def metodoBurbujaMejorado(arreglo):
    print("Muy bien usted a escogido el metodo de burbuja mejorado")
    llenarArreglo(arreglo)
    imprimirArreglo(arreglo)
    for i in range(1,5):
        #Utilizamos la bandera como un auxiliar extra para evitar recorrer el arreglo si ya esta ordenado 
        bandera = 0 #y se inicia en 0
        for j in range(0,5-i):
            if(arreglo[j]>arreglo[j+1]):
                aux = arreglo[j]
                arreglo[j] = arreglo[j+1]
                arreglo[j+1] = aux
                bandera = 1#Si hubo algun cambio la bandera se iguala a 0
        if(bandera == 0):
            break#Si no hubo cambios se acaba el for
    print("Muy bien he acabado de ordenar el arreglo, y ha quedado asi:")
    imprimirArreglo(arreglo)

#Imprimimos el tiempo que tomo ejecutar el programa
def tiempo(inicio):
    fin = time.time()
    tiempo_ejecutado = fin - inicio
    print(f'Vaya si que fue un poco tardado me tarde: {tiempo_ejecutado}')

print("Hola este programa Ordena numeros que usted ocupe mediante dos metodos")
print("1)Metodo de burbuja\n2)Metodo de burbuja mejorado")
op = int(input("Cuantos opcion desea ocupar? "))
if(op == 1):
    metodoBurbuja(arreglo)
elif(op == 2):
    metodoBurbujaMejorado(arreglo)
else:
    print("Error opcion invalida")
    