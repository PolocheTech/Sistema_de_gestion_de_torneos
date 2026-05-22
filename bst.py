class nodo_bst():

    def __init__(self, nombre_jugador, puntaje):
        self.jugador = nombre_jugador
        self.puntaje = puntaje
        self.izquierda = None
        self.derecha = None

class BST():
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre_jugador, puntaje):
        actual = None
        padre = None
        
        while actual is not None:
            padre = actual