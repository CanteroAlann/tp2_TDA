import sys
import os
import file_reader
import lista_circular


if len(sys.argv) != 2:
    print("Uso: python arturo.py cablleros.txt")
    sys.exit(1)


def main():
    OPTIMO_CABALLEROS = []

    archivo_de_caballeros = sys.argv[1]
    caballeros = file_reader.leer_archivo(archivo_de_caballeros)
    caballeros.mostrar()


if __name__ == "__main__":
    main()
