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
                grafo.agregar_vertice(servidor1)
                grafo.agregar_vertice(servidor2)
                grafo.agregar_arista(servidor1, servidor2, int(velocidad))
                # Agrego este vertice ficticio para eliminar arista antiparalela (la conexion es bidireccional)
                # respetando su existencia en el grafo original
                vertice_ficticio = 'ficticio de ' + servidor2 + ' a ' + servidor1
                grafo.agregar_vertice(vertice_ficticio)
                grafo.agregar_arista(servidor2, vertice_ficticio, int(velocidad))
                grafo.agregar_arista(vertice_ficticio, servidor1, int(velocidad))

    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        sys.exit(1)
    return grafo


