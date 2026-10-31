class Nodo:

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None


class ListEnlazada:

    def __init__(self):
        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)
        # Si la lista está vacía, siguiente queda en None y cabeza apunta al nuevo nodo.
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)

        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_al_Inicio(self):
        # Lista vacía: no hay nada que eliminar
        if self.cabeza is None:
            print("La lista está vacía, no hay nodo que eliminar.")
            return

        # La cabeza pasa a ser el segundo nodo
        self.cabeza = self.cabeza.siguiente

    def Eliminar_Nodo_al_Final(self):
        # Lista vacía
        if self.cabeza is None:
            print("La lista está vacía, no hay nodo que eliminar.")
            return

        # Un solo nodo: la lista queda vacía
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return

        # Recorrer hasta el penúltimo nodo
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente

        actual.siguiente = None

    def Imprimir_ListaEnlazada(self):
        actual = self.cabeza

        while actual:
            print(actual.numero, "->", end=" ")
            actual = actual.siguiente

        print("None")


Mi_lista = ListEnlazada()
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Final(56)
print("Lista original:")
Mi_lista.Imprimir_ListaEnlazada()         

Mi_lista.Eliminar_Nodo_al_Inicio()
print("Después de eliminar al inicio:")
Mi_lista.Imprimir_ListaEnlazada()         

Mi_lista.Eliminar_Nodo_al_Final()
print("Después de eliminar al final:")
Mi_lista.Imprimir_ListaEnlazada()          