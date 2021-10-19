from grafo import Grafo
import heapq

def dijkstra(grafo, origen):
    dist= {}
    padre = {}
    for v in grafo:
        dist[v] = float("inf")
    dist[origen] = 0
    padre[origen] = None

    heap = []
    heapq.heappush(heap,(0, origen))
    while heap:
        distancia, v = heapq.heappop(heap)
        for w in grafo.adyacentes(v):
            if dist[v] + grafo.peso_arista(v,w) < dist[w]:
                dist[w] = dist[v] + grafo.peso_arista(v,w)
                padre[w] = v
                heapq.heappush(heap,(dist[w], w))

    return padre, dist


g = Grafo(True)
g.agregar_vertice('a')
g.agregar_vertice('b')
g.agregar_vertice('c')
g.agregar_vertice('d')
g.agregar_vertice('e')
g.agregar_arista('a','b',1)
g.agregar_arista('b','c',3)
g.agregar_arista('c','e',5)
g.agregar_arista('e','a',2)
g.agregar_arista('c','d',3)


print(dijkstra(g,'a'))

