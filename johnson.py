from Dijkstra import dijkstra
from copy import deepcopy
from BellmanFord import bellman_ford, obtener_aristas
from grafo import Grafo

def johnson(grafo):
	grafo.agregar_vertice("inicio")
	for nodo in grafo:
		grafo.agregar_arista("inicio", nodo, 0)

	distancia, padres = bellman_ford(grafo, "inicio")
	padres.pop("inicio")
	grafo_nuevo = deepcopy(grafo)

	aristas = obtener_aristas(grafo)

	for i,j in aristas:
		peso_anterior = grafo.peso_arista(i,j)
		grafo_nuevo.cambiar_peso(i, j, peso_anterior + distancia[i] - distancia[j])

	grafo_nuevo.borrar_vertice("inicio")

	distancias_minimas = {}
	for nodo in grafo_nuevo:
		distancias_minimas[nodo] = dijkstra(grafo_nuevo, nodo)

	return distancias_minimas