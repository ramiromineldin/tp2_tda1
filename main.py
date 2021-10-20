from grafo import Grafo
from johnson import johnson

mapa_depositos = Grafo(True)
with open("depositos.txt", "r") as archivo:
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		mapa_depositos.agregar_vertice(info[0])
		mapa_depositos.agregar_vertice(info[1])
		mapa_depositos.agregar_arista(info[0],info[1],int(info[2]))

distancias_minimas = johnson(mapa_depositos)
sumas = {}
for i in distancias_minimas:
	for j in distancias_minimas[i]:
		sumas[i] += distancias_minimas[i][j] 