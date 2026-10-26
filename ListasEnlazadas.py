class Nodo:

    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

class ListEnlazada:

    def __init__(self):

        self.cabeza = None

    def Insertar_Nodo_al_Inicio(self, numero):

        nuevo_nodo = Nodo(numero)

        if(self.cabeza is Nodo):

            self.cabeza = Nodo(numero)

            return

        nuevo_nodo.siguiente = self.cabeza

        self.cabeza = nuevo_nodo

    def Insertar_Nodo_al_Final(self, numero):

        nuevo_nodo = Nodo (numero)

        if(self.cabeza == None):

            self.cabeza = nuevo_nodo 

            return

        actual = self.cabeza

        while(actual.siguiente):

            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Imprimir_ListaEnlazada(self):

        actual = self.cabeza

        while(actual):

            print(actual.numero, "->", end = " ")

            actual = actual.siguiente

        print("None")
                        
Mi_lista = ListEnlazada()
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Final(56)
Mi_lista.Imprimir_ListaEnlazada()