"""Funcion para leer los archivos pasados por parametro"""
import sys
from grafo import Grafo

def leer_archivo(archivo):
    try:
        with open(archivo, 'r') as archivo:
            grafo = []
    
            for linea in archivo:
                servidor1, servidor2, velocidad = linea.strip().split(',')
                popularidad = int(popularidad)
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        sys.exit(1)
    return grafo