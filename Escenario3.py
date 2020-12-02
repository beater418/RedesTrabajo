class Vertice:
    def __init__(self, numerovertice):
        self.numV = numerovertice;
        self.adyacentes = [];               #arreglo de vertices adyacentes
        self.padre = None;                  #Indica el padre precesor se incializa en el None
        self.visitado= False;
        self.distancia = float('inf');      #Sirve para incializar la distancia del vertice en infinito al momento de ser creado

    def agregarVerticesAdy(self, vertice, peso):
        if vertice not in self.adyacentes:
            self.adyacentes.append([vertice, peso])

class Grafo: 
    def __init__(self):
        self.vertices = {};

    def crearVertice(self, numV):                   #Se agrega el vertice (su numero o id) en la lista de vertices
        if numV not in self.vertices:
            self.vertices[numV] = Vertice(numV);

    def agregarArista(self, vertice1, vertice2, peso):
        if vertice1 in self.vertices and vertice2  in self.vertices:
            self.vertices[vertice1 ].agregarVerticesAdy(vertice2, peso);
            self.vertices[vertice2].agregarVerticesAdy(vertice1 , peso);

    def camino(self, vertice1, vertice2): #Trazamos la ruta que deseamos recorrer indicando el nodo de incio y el nodo final en la clase main
        camino = [];
        actual = vertice2;
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[vertice2].distancia]

    def minimo(self, lista): #Calculamos la distancia menor mas tentativa entre los nodos no visitados
        if len(lista) > 0:
            x = self.vertices[lista[0]].distancia;
            y = lista[0];
            for elemento in lista:
                if x > self.vertices[elemento].distancia:
                    x = self.vertices[elemento].distancia
                    y = elemento
            return y
    

    def dijkstra(self, a):       #a es vertice actual
        if a in self.vertices:
            self.vertices[a].distancia = 0;
            actual = a;
            verticesnoVisitados = [];

            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia= float('inf');
                self.vertices[v].padre = None;
                verticesnoVisitados.append(v);


            while len(verticesnoVisitados) > 0: #Calculamos la distancia  del nodo actual + el peso actual
                for vecino in self.vertices[actual].adyacentes:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual


                self.vertices[actual].visitado = True;
                verticesnoVisitados.remove(actual); #Se elimina al nodo actual de lista de no visitados
                actual = self.minimo(verticesnoVisitados);


        else:
            return False;


import time
import random 
class main: #Ejecutamos el grafo , creamos los vertices y las ristas con sus pesos
    g = Grafo()
    g.crearVertice(0)
    g.crearVertice(1)
    g.crearVertice(2)
    g.crearVertice(3)
    g.crearVertice(4)
    g.crearVertice(5)
    g.crearVertice(6)
    g.crearVertice(7)
    g.crearVertice(8)
    g.crearVertice(9)
    g.crearVertice(10)
    g.crearVertice(11)
    g.crearVertice(12)
    g.crearVertice(13)
    g.crearVertice(14)
    g.crearVertice(15)
    g.crearVertice(16)
    g.crearVertice(17)
    g.crearVertice(18)
    g.crearVertice(19)
    g.crearVertice(20)

    g.agregarArista(0,1,2)
    g.agregarArista(0,4,2)

    g.agregarArista(1,3,2)
    g.agregarArista(1,1,1)

    g.agregarArista(4,1,3)
    g.agregarArista(4,2,2)
    g.agregarArista(4,6,2)
    g.agregarArista(4,8,4)

    g.agregarArista(6,2,4)

    g.agregarArista(2,0,3)

    g.agregarArista(3,4,6)
    g.agregarArista(3,8,3)
    g.agregarArista(3,7,5)

    g.agregarArista(8,7,6)
    g.agregarArista(8,11,3)
    g.agregarArista(8,9,5)
    g.agregarArista(8,5,3)

    g.agregarArista(5,4,1)
    g.agregarArista(5,6,1)

    g.agregarArista(9,5,1)
    g.agregarArista(9,11,8)
    g.agregarArista(9,14,8)
    g.agregarArista(9,15,8)

    g.agregarArista(7,10,2)
    g.agregarArista(7,13,4)
    g.agregarArista(7,11,3)

    g.agregarArista(10,10,1)

    g.agregarArista(13,16,5)

    g.agregarArista(11,12,3)
    g.agregarArista(11,14,8)

    g.agregarArista(14,12,2)
    g.agregarArista(14,17,4)
    g.agregarArista(14,15,4)

    g.agregarArista(15,17,2)
    g.agregarArista(15,18,8)
    g.agregarArista(15,19,1)

    g.agregarArista(17,16,1)
    g.agregarArista(17,18,3)

    g.agregarArista(16,20,4)

    g.agregarArista(18,20,5)
    g.agregarArista(18,19,1)
    
    g.agregarArista(19,20,1)
  
    print("\n\nLa ruta más rapida por Djikstra junto con su costo es :")
    g.dijkstra(0)
    print(g.camino(0,20))
  




