from Dijkstra import dijkstra
from copy import deepcopy
from BellmanFord import bellman_ford, obtener_aristas
from grafo import Grafo

def johnson(mapa_depositos):
	mapa_depositos.agregar_vertice("inicio")
	for nodo in mapa_depositos:
		mapa_depositos.agregar_arista("inicio", nodo, 0)

	distancia, padres = bellman_ford(mapa_depositos, "inicio")
	padres.pop("inicio")

	mapa_depositos_actualizado = deepcopy(mapa_depositos)

	aristas = obtener_aristas(mapa_depositos)

	for i,j in aristas:
		peso_anterior = mapa_depositos.peso_arista(i,j)
		mapa_depositos_actualizado.cambiar_peso(i, j, peso_anterior + distancia[i] - distancia[j])

	mapa_depositos_actualizado.borrar_vertice("inicio")
	#print(("mapa: {}").format(mapa_depositos_actualizado))

	distancias_minimas = {}
	for nodo in mapa_depositos_actualizado:
		distancias_minimas[nodo] = dijkstra(mapa_depositos_actualizado, nodo)

	return distancias_minimas