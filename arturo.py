
def maxima_habilidad_caballero(caballeros):
    caballeros_circular = caballeros + caballeros
    c = 0
    
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
    return max_habilidad, caballeros_elegidos_global

caballeros = [("Bors", 8), ("Gawain", -8), ("Percival", 9), ("Pellinor", -9), ("Galahad", -10), ("Gareth", -11), ("Lancelot",12)]
print(maxima_habilidad_caballero(caballeros))

