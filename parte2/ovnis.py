import sys
import os
import file_reader as file_reader
import copy


if len(sys.argv) != 2:
    sys.exit(1)

def obtener_flujo_maximo(red, fuente, sumidero):
    flujo = {}
    for v in red.obtener_vertices():
        for w in red.adyacentes(v):
            flujo[(v, w)] = 0
    grafo_residual = copy.deepcopy(red)
    camino = obtener_camino(grafo_residual, fuente, sumidero)
    while camino is not None:
        bottleneck = min_peso(red, camino)
        for i in range(1, len(camino)):
            if red.son_adyacentes(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += int(bottleneck)
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], int(bottleneck))
            else:
                flujo[(camino[i], camino[i-1])] -= bottleneck
                actualizar_grafo_residual(grafo_residual, camino[i], camino[i-1], int(bottleneck))

        camino = obtener_camino(grafo_residual, fuente, sumidero)
    return flujo



    

def actualizar_grafo_residual(grafo_residual, v, w, bottleneck):
    peso_anterior = grafo_residual.peso_arista(v, w)
    if peso_anterior == bottleneck:
        grafo_residual.borrar_arista(v, w)
    else:
        grafo_residual.cambiar_peso_arista(v, w, peso_anterior - bottleneck)
    if not grafo_residual.son_adyacentes(w, v):
        grafo_residual.agregar_arista(w, v, bottleneck)
    else:
        grafo_residual.cambiar_peso_arista(w, v, peso_anterior + bottleneck)



def obtener_camino(red, fuente, sumidero):
    # Crear una copia de la red para trabajar con ella sin modificar la original
    red_residual = copy.deepcopy(red)

    # Inicializar una lista para realizar el recorrido BFS
    cola = [(fuente, [fuente])]

    # Mientras haya nodos en la cola
    while cola:
        nodo_actual, camino_actual = cola.pop(0)

        # Obtener los vecinos del nodo actual en la red residual
        vecinos = red_residual.adyacentes(nodo_actual)

        for vecino in vecinos:
            # Obtener la capacidad residual de la arista
            capacidad_residual = red_residual.peso_arista(nodo_actual, vecino)

            # Si la capacidad residual es mayor que cero, significa que hay un camino
            # válido en la red residual
            if capacidad_residual > 0:
                # Agregar el vecino al camino actual
                nuevo_camino = camino_actual + [vecino]

                # Si hemos llegado al sumidero, hemos encontrado un camino
                if vecino == sumidero:
                    return nuevo_camino

                # Agregar el vecino y su camino al final de la cola para seguir buscando
                cola.append((vecino, nuevo_camino))

                # Marcar la arista como visitada eliminando la capacidad en la red residual
                red_residual.borrar_arista(nodo_actual, vecino)

    # Si no se encuentra ningún camino válido, retornar None
    return None
    


def min_peso(red, camino):
    return min(camino)


def main():
    archivo_red_servidores = sys.argv[1]
    red = file_reader.leer_archivo(archivo_red_servidores)
    print(obtener_flujo_maximo(red, 'R', 'S'))

if __name__ == "__main__":
    main()