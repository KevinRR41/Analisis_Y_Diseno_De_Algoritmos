import time
import heapq
#Creamos la clase
class Graph:
    #Constructor self  Vertex = Vertice / Edge = Arista
    def __init__(self):
        self.vertex = set ()
        self.edge = {}
    #Funcion para agregar vertices
    def  addVertex(self, value):
        self.vertex.add(value)
        self.edge[value] = []
    #Funcion para agregar aristas from = desde / until = hasta / weight = peso
    def addEdge(self, From, until, weight):
        self.edge[From].append((until, weight))
        #Si el grafo es no dirigido
        self.edge[until].append((From, weight))
    def dijkstra(self, begin):
    #Inicializando el diccionario
        distance = {v: float('infinity') for v in self. vertex}
        distance[begin] = 0
    #Se usa un heap para tomar el vertice con la distancia minima mejor eficiente
        reir_priority = [(0, begin)]
        #Inciamos el tiempo
        begin_time = time.time()
        
        while reir_priority:
            distance_present, vertex_present = heapq.heappop(reir_priority)
            #Si la distancia que esta actual es mayor a la que esta en el diccionario, se cambia al siguiente vertice
            if distance_present > distance[vertex_present]:
                continue

            #Recorrer los vertices vecinos del vertice actual   
            for neighbor, weight in self.edge[vertex_present]:
                distance_new = distance_present + weight

                #Se cambian las distancisa minimas si hay un camino mas corto
                if distance_new < distance[neighbor]:
                    distance[neighbor] = distance_new
                    heapq.heappush(reir_priority, (distance_new, neighbor))
            #Detenemos y calculamos el tiempo
            end_time = time.time()
            time_carry = end_time - begin_time
        #Devuelve el tiempo y el diccionario
        return distance, time_carry

if __name__ == '__main__':
    #Creamos el grafo que queremos usar
    Graph_example = Graph()
    #Agregamos los vertices
    Graph_example.addVertex('A')
    Graph_example.addVertex('B')
    Graph_example.addVertex('C')
    Graph_example.addVertex('D')
    #Agregamos las aristas
    Graph_example.addEdge('A', 'B', 2)
    Graph_example.addEdge('A', 'C', 3)
    Graph_example.addEdge('A', 'D', 9)
    Graph_example.addEdge('B', 'C', 8)  
    Graph_example.addEdge('B', 'D', 3)
    Graph_example.addEdge('C', 'D', 6)
    #Tomamos nuestro vertice de inicio
    begin_vertex = 'A'
    #Aplicamos dijkstra al grafo
    distance_minimum, time_carry= Graph_example.dijkstra(begin_vertex)
    #Lo imprimimos
    print(f'Las distancias minimas desde el vertice de comienzo {begin_vertex} es : {distance_minimum}')
    print(f'Tiempo de ejecución: {time_carry} segundos')

    # Calculamos la complejidad
    v = len(Graph_example.vertex)
    e = sum(len(edges) for edges in Graph_example.edge.values())
    #El algoritmo tiene una complejidad en el tiempo donde V es el número de vértices y E es el número de aristas 
    print(f'Complejidad de tiempo: O((V + E) log V) = O(({v} + {e}) log {v})')