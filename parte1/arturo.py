import sys
import os
import file_reader as file_reader

if len(sys.argv) != 2:
    sys.exit(1)



def maxima_habilidad_caballero(caballeros):
    if len(caballeros) == 0:
        return []
    caballeros_circular = caballeros + caballeros    
    optimos = [0 for _ in range(len(caballeros_circular))]
    optimos[0] = caballeros[0][1]
    max_habilidad = optimos[0]
    caballeros_elegidos_local = [caballeros[0][0]]
    caballeros_elegidos_global = [caballeros[0][0]]
    c = 1
    for i in range(1, len(caballeros_circular)):
        if optimos[i-1] + caballeros_circular[i][1] > caballeros_circular[i][1]:
            optimos[i] = optimos[i-1] + caballeros_circular[i][1]
            caballeros_elegidos_local.append(caballeros_circular[i][0])            
            if optimos[i] > max_habilidad:
                caballeros_elegidos_global = caballeros_elegidos_local[:]
                max_habilidad = optimos[i]
            c += 1
        else:
            optimos[i] = caballeros_circular[i][1]
            caballeros_elegidos_local = [caballeros_circular[i][0]]
            if optimos[i] > max_habilidad:
                caballeros_elegidos_global = [caballeros_circular[i][0]]
                max_habilidad = optimos[i]
            c = 1
        if c == caballeros_elegidos_local:
            break
    return caballeros_elegidos_global




def main():
    archivo_caballeros = sys.argv[1]
    caballeros = file_reader.leer_archivo(archivo_caballeros)
    print(maxima_habilidad_caballero(caballeros))

if __name__ == "__main__":
    main()