import sys
import file_reader as file_reader

if len(sys.argv) != 2:
    print("Uso: python3 arturo.py <archivo_caballeros>")
    sys.exit(1)

def maximo_subarray_contiguo_lineal(caballeros):
    n = len(caballeros)
    if n == 0:
        return []
    max_global = caballeros[0][1]
    max_local = caballeros[0][1]
    start = 0
    end = 0
    for i in range(1, n):
        if max_local + caballeros[i][1] > caballeros[i][1]:
            max_local = max_local + caballeros[i][1]
            if max_local > max_global:
                max_global = max_local
                end = i
        else:
            max_local = caballeros[i][1]
            if max_local > max_global:
                max_global = max_local
                start = i
                end = i
    return max_global, start, end + 1

def minimo_subarray_contiguo_lineal(caballeros):
    n = len(caballeros)
    if n == 0:
        return []
    min_global = caballeros[0][1]
    min_local = caballeros[0][1]
    start = 0
    end = 0
    for i in range(1, n):
        if min_local + caballeros[i][1] < caballeros[i][1]:
            min_local = min_local + caballeros[i][1]
            if min_local < min_global:
                min_global = min_local
                end = i
        else:
            min_local = caballeros[i][1]
            if min_local < min_global:
                min_global = min_local
                start = i
                end = i
    return min_global, start, end + 1

def obtener_caballeros_con_mayor_hablidad(caballeros):
    n = len(caballeros)
    if n == 0:
        return []
    maxima_hablidad_lineal, start_max, end_max = maximo_subarray_contiguo_lineal(caballeros)
    minima_hablidad_lineal, start_min, end_min = minimo_subarray_contiguo_lineal(caballeros)
    suma_hablidades = sum(caballero[1] for caballero in caballeros)
    son_todas_las_hablidades_negativas = (suma_hablidades - minima_hablidad_lineal == 0)
    if maxima_hablidad_lineal > (suma_hablidades - minima_hablidad_lineal) or son_todas_las_hablidades_negativas:
        caballeros_seleccionados = caballeros[start_max:end_max]
        return [caballero[0] for caballero in caballeros_seleccionados]
    else:
        caballeros_seleccionados = caballeros[end_min:] + caballeros[:start_min]
        return [caballero[0] for caballero in caballeros_seleccionados]

    


def main():
    archivo_caballeros = sys.argv[1]
    caballeros = file_reader.leer_archivo(archivo_caballeros)
    print(obtener_caballeros_con_mayor_hablidad(caballeros))

if __name__ == "__main__":
    main()
