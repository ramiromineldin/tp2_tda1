from grafo import Grafo
from johnson import johnson
import sys


def pretty_print():
    sys.stdout.write("  ")
    print(' '.join(distancias_minimas.keys()))
    for key in distancias_minimas.keys():
        values = distancias_minimas.get(key)
        sys.stdout.write(key)
        sys.stdout.write(" ")
        for value in values.keys():
            sys.stdout.write(values.get(value).__str__())
            sys.stdout.write(" ")

        print
        sys.stdout.write("\n")

mapa_ciudades = Grafo(True)
nombre_arch = input("Ingrese el nombre del archivo de depositos que desea procesar (sin extension): ")
nombre_arch_extension = nombre_arch + ".txt"

with open(nombre_arch_extension, "r") as archivo:
	for linea in archivo:
		info = linea.replace("\r\n","").split(',')
		mapa_ciudades.agregar_vertice(info[0])
		mapa_ciudades.agregar_vertice(info[1])
		mapa_ciudades.agregar_arista(info[0],info[1],int(info[2]))

distancias_minimas = johnson(mapa_ciudades)

print("La solucion de Johnson es: ")
pretty_print()

sumas = {}
for i in distancias_minimas:
	sumas[i] = 0
	for j in distancias_minimas[i]:
		sumas[i] = sumas[i] + distancias_minimas[i][j]

ciudad_elegida = min(sumas, key=sumas.get)

ciudades = []
for nodo in sumas:
	if sumas[nodo] == sumas[ciudad_elegida]:
		ciudades.append(nodo)

print(("La/s ciudad/es donde deberia ubicarse la fabrica es: {}").format(', '.join(ciudades)))
