class nodo_bst():

    def __init__(self, jugador, puntaje):
        self.jugador = jugador
        self.puntaje = puntaje
        self.izquierdo = None
        self.derecho = None

class BST():
    
    def __init__(self):
        self.raiz = None

    def insertar(self, jugador, puntaje):
        self.raiz = self._insertar(self.raiz, jugador, puntaje)

    def _insertar(self, nodo, jugador, puntaje):
        if nodo is None:
            return nodo_bst(jugador, puntaje)
        
        if puntaje < nodo.puntaje:
            nodo.izquierdo = self._insertar(nodo.izquierdo, jugador, puntaje)
        
        elif puntaje > nodo.puntaje:
            nodo.derecho = self._insertar(nodo.derecho, jugador, puntaje)
        
        return nodo

    def inorden(self):
        resultado = []
        self._inorden(self.raiz, resultado)
        return resultado

    def _inorden(self, nodo, res):
        if nodo:
            self._inorden(nodo.izquierdo, res)
            res.append((nodo.jugador, nodo.puntaje))
            self._inorden(nodo.derecho, res)

    def buscar(self, puntaje):
        return self._buscar(self.raiz, puntaje)
    
    def _buscar(self, nodo, puntaje):
        if nodo is None:
            return "Jugador no encontrado"
        
        if puntaje == nodo.puntaje:
            return nodo.jugador, nodo.puntaje
    
        if puntaje < nodo.puntaje:
            return self._buscar(nodo.izquierdo, puntaje)
        
        return self._buscar(nodo.derecho, puntaje)


if __name__ == "__main__":
    arbol = BST()
    arbol.insertar("NinjaX", 50)
    arbol.insertar("JuanPro", 100)
    arbol.insertar("AnaGamer", 200)
    arbol.insertar("ShadowK", 75)

    print(arbol.buscar(75))    # → ('ShadowK', 75)
    print(arbol.buscar(100))   # → ('JuanPro', 100)
    print(arbol.buscar(999))   # → 'Jugador no encontrado'