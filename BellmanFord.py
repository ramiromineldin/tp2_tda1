from grafo import Grafo


def bellman_ford(grafo, inicio):
    distancias = {}
    distancia = [None] * (len(grafo.obtener_vertices()))
    vertices = grafo.obtener_vertices()

    for v in vertices:
        distancia[vertices.index(v)] = float("inf")
        distancia[vertices.index(inicio)] = 0

    for _ in range(1, len(vertices)):
        for vertice in vertices:
            adyacentes = grafo.adyacentes(vertice)
            v = vertices.index(vertice)
            for adyacente in adyacentes:
                a = vertices.index(adyacente)
                peso = grafo.peso_arista(vertice, adyacente)
                if distancia[v] + peso < distancia[a]:
                    distancia[a] = distancia[v] + peso
                    distancias["distancia " + adyacente + "-" + inicio] = distancia[a]

    for vertice in vertices:
        adyacentes = grafo.adyacentes(vertice)
        if len(adyacentes) > 0:
            adyacente = grafo.adyacentes(vertice)[0]
            peso = grafo.peso_arista(vertice, adyacente)

            if distancia[vertices.index(vertice)] + peso < distancia[vertices.index(adyacente)]:
                print("Ciclo negativo!!!")

    print(distancia)
    print(distancias)
    return distancia


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

print(bellman_ford(g,'a'))
