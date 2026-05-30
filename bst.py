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

    def eliminar(self, puntaje):
        self.raiz = self._eliminar(self.raiz, puntaje)

    def _eliminar(self, nodo, puntaje):
        # Caso base: jugador no encontrado
        if nodo is None:
            return "Jugador no encontrado"

        # Caminar por el árbol (igual que en buscar)
        if puntaje < nodo.puntaje:
            nodo.izquierdo = self._eliminar(nodo.izquierdo, puntaje)
        elif puntaje > nodo.puntaje:
            nodo.derecho = self._eliminar(nodo.derecho, puntaje)
        else:
            # Encontré el nodo → aquí van los 3 casos

            # Caso 1: sin hijos
            if nodo.izquierdo is None and nodo.derecho is None:
                return None

            # Caso 2: un solo hijo
            elif nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            # Caso 3: dos hijos
            else:
                # buscar el mínimo del subárbol derecho
                # copiar sus datos
                # eliminar el sucesor

                sucesor = self._minimo(nodo.derecho)
                nodo.jugador = sucesor.jugador
                nodo.puntaje = sucesor.puntaje

                nodo.derecho = self._eliminar(nodo.derecho, sucesor.puntaje)

        return nodo

    def _minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo