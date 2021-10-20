from grafo import Grafo
def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v,w))
    return aristas


def bellman_ford(grafo, origen):
    distancia = {}
    padres = {}
    aristas = obtener_aristas(grafo)
    for v in grafo:
        distancia[v] = float("inf")
    distancia[origen] = 0
    padres[origen] = None

    for i in range(len(grafo)):
        for v,w in aristas:
            if distancia[w] > distancia[v] + grafo.peso_arista(v,w):
                distancia[w] = distancia[v] + grafo.peso_arista(v,w)
                padres[w] = v

    for v,w in aristas:
        if distancia[w] > distancia[v] + grafo.peso_arista(v,w):
            print ("hay ciclo negativo")
            return False
    print(distancia)
    return True

