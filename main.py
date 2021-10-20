from grafo import Grafo
from johnson import johnson

mapa_ciudades = Grafo(True)
with open("depositos.txt", "r") as archivo:
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		mapa_ciudades.agregar_vertice(info[0])
		mapa_ciudades.agregar_vertice(info[1])
		mapa_ciudades.agregar_arista(info[0],info[1],int(info[2]))

distancias_minimas = johnson(mapa_ciudades)

print("La solucion de Johnson es: ")
print(distancias_minimas)

sumas = {}
for i in distancias_minimas:
	sumas[i] = 0
	for j in distancias_minimas[i]:
		sumas[i] = sumas[i] + distancias_minimas[i][j]


ciudad_elegida = min(sumas, key=sumas.get)

print(("La ciudad donde deberia ubicarse en el deposito es: {}").format(ciudad_elegida))