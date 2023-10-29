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
        bottleneck = min_peso(grafo_residual, camino)
        for i in range(1, len(camino)):
            if red.son_adyacentes(camino[i-1], camino[i]):
                flujo[(camino[i-1], camino[i])] += int(bottleneck)
                actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], int(bottleneck))
            else:
                flujo[(camino[i], camino[i-1])] -= bottleneck
                actualizar_grafo_residual(grafo_residual, camino[i], camino[i-1], int(bottleneck))

        camino = obtener_camino(grafo_residual, fuente, sumidero)
    



    return flujo, grafo_residual



    

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
    '''Obtiene un camino entre la fuente y el sumidero en la red residual (BFS)'''
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
    
def corte_minimo(red, grafo_residual):
    '''Busco las conexiones que se cortan'''
    nodos_alcanzables = set()
    cola = ['R']

    # Realizar un recorrido BFS en el grafo residual para encontrar los nodos alcanzables desde la fuente
    while cola:
        nodo_actual = cola.pop(0)
        nodos_alcanzables.add(nodo_actual)
        for adyacente in grafo_residual.adyacentes(nodo_actual):
            if adyacente not in nodos_alcanzables:
                cola.append(adyacente)

    corte = set()
    for nodo in nodos_alcanzables:
        for adyacente in red.adyacentes(nodo):
            if adyacente not in nodos_alcanzables:
                corte.add((nodo, adyacente))

    return corte
    
def min_peso(red, camino):
    '''Busco el bottleneck minimo flujo que puedo enviar por eso camino'''
    pesos = []
    for i in range(1, len(camino)):
        pesos.append(red.peso_arista(camino[i-1], camino[i]))
    return min(pesos)


def mostrar_configuracion_conexiones(flujo):
    '''Muestra las configuraciones de conexiones'''
    for conexion in flujo:
        if flujo[conexion] > 0:
            print(f"{conexion[0]}  -- {flujo[conexion]} -->  {conexion[1]}")

def main():
    archivo_red_servidores = sys.argv[1]
    red = file_reader.leer_archivo(archivo_red_servidores)
    flujo, grafo_residual = obtener_flujo_maximo(red, 'R', 'S')
    mostrar_configuracion_conexiones(flujo)
    print(corte_minimo(red, grafo_residual))

if __name__ == "__main__":
    main()