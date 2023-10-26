"""Funcion para leer los archivos pasados por parametro"""
import sys

def leer_archivo(archivo):
    try:
        with open(archivo, 'r') as archivo:
            caballeros = []
    
            for linea in archivo:
                nombre, popularidad = linea.strip().split(',')
                popularidad = int(popularidad)
                caballeros.append((nombre, popularidad))
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        sys.exit(1)
    return caballeros