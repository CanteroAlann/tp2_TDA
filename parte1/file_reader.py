import sys
import lista_circular


def leer_archivo(archivo):
    try:
        with open(archivo, "r") as archivo:
            # Inicializa una lista vacía para almacenar los elementos
            lista_circular_de_elementos = lista_circular.ListaCircular()

            # Lee cada línea del archivo
            for linea in archivo:
                # Limpia la línea (quita caracteres especiales como '\n')
                # y separa los elementos por comas
                elemento = linea.strip().split(",")

                nuevo_nodo = lista_circular.Nodo(elemento)

                # Agrega el elemento a la lista
                lista_circular_de_elementos.agregar(elemento)
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encuentra.")
        sys.exit(1)
    return lista_circular_de_elementos
