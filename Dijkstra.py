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

    return dist

