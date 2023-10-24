class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cabeza.siguiente = self.cabeza
        else:
            nuevo_nodo.siguiente = self.cabeza.siguiente
            self.cabeza.siguiente = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar(self, valor):
        if not self.cabeza:
            return

        nodo_actual = self.cabeza
        while nodo_actual.siguiente != self.cabeza:
            if nodo_actual.siguiente.valor == valor:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                return
            nodo_actual = nodo_actual.siguiente

    def mostrar(self):
        if not self.cabeza:
            return

        nodo_actual = self.cabeza
        while True:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.cabeza:
                break
        print()
