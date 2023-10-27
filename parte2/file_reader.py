"""Funcion para leer los archivos pasados por parametro"""
import sys
from grafo import Grafo

def leer_archivo(archivo):
    try:
        with open(archivo, 'r') as archivo:
            # creo grafo dirigido
            grafo = Grafo(True)
            for linea in archivo:
                servidor1, servidor2, velocidad = linea.strip().split(',')
                if servidor1 == 'S' or servidor2 == 'R':
                    # Si hay un eje que sale de S o llega a R, no lo agrego
                    continue
                grafo.agregar_vertice(servidor1)
                grafo.agregar_vertice(servidor2)
                grafo.agregar_arista(servidor1, servidor2, int(velocidad))
                # si el servidor1 es R o el servidor2 es S, no agrego la arista antiparalela (no tiene sentido en el problema)
                if servidor1 != 'R' and servidor2 != 'S':
                    # Agrego este vertice ficticio para eliminar arista antiparalela (la conexion es bidireccional)
                    # respetando su existencia en el grafo original
                    vertice_ficticio = 'vertice ficticio de ' + servidor2 + ' a ' + servidor1
                    grafo.agregar_vertice(vertice_ficticio)
                    grafo.agregar_arista(servidor2, vertice_ficticio, int(velocidad))
                    grafo.agregar_arista(vertice_ficticio, servidor1, int(velocidad))

    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        sys.exit(1)
    return grafo


