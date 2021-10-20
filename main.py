from grafo import Grafo
from Dijkstra importa dijkstra 

mapa_depositos = Grafo(True)
with open("depositos.txt", "r") as archivo:
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		mapa_depositos.agregar_vertice(info[0])
		mapa_depositos.agregar_vertice(info[1])
		mapa_depositos.agregar_arista(info[0],info[1],int(info[2]))

mapa_depositos.agregar_vertice("inicio")
for nodo in mapa_depositos:
	mapa_depositos.agregar_arista("inicio", nodo, 0)