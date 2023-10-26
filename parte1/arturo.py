import sys
import os
import file_reader as file_reader

if len(sys.argv) != 2:
    sys.exit(1)


def maxima_habilidad_caballero(caballeros):
    if len(caballeros) == 0:
        return []
    caballeros_circular = caballeros + caballeros    
    max_global = caballeros_circular[0][1]
    max_local = caballeros_circular[0][1]
    start = 0
    end = 0
    c = 1
    for i in range(1, len(caballeros_circular)):
        if max_local + caballeros_circular[i][1] > caballeros_circular[i][1]:
            max_local = max_local + caballeros_circular[i][1]
            if max_local > max_global:
                max_global = max_local
                end = i
            c += 1
        else:
            max_local = caballeros_circular[i][1]
            if max_local > max_global:
                max_global = max_local
                start = i
                end = i
            c = 1
        if c == len(caballeros):
            break
    return [caballero[0] for caballero in caballeros_circular[start:end+1]]






def main():
    archivo_caballeros = sys.argv[1]
    caballeros = file_reader.leer_archivo(archivo_caballeros)
    print(maxima_habilidad_caballero(caballeros))

if __name__ == "__main__":
    main()