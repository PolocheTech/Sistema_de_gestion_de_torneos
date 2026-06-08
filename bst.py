class nodo_bst():
    # clase constructora de la clase - nodo_bst().
    # Crea un nodo del árbol con nombre de jugador y su puntaje.
    def __init__(self, jugador, puntaje):
        self.jugador = jugador
        self.puntaje = puntaje
        self.izquierdo = None
        self.derecho = None

class BST():
    
    def __init__(self):
        # Inicializa el árbol vacio con (self.raiz = None)
        self.raiz = None


    # Esta funcion inserta un jugador en el árbol usando su puntaje como clave.
    # Llama a (_insertar) para hacer la insercion recursiva.  
    def insertar(self, jugador, puntaje):
        self.raiz = self._insertar(self.raiz, jugador, puntaje)


    def _insertar(self, nodo, jugador, puntaje):
        if nodo is None: # Si el nodo actual es None, crea un nodo nuevo.
            return nodo_bst(jugador, puntaje)
        
        if puntaje < nodo.puntaje: # Si el puntaje es menor, intenta insertar en el subárbol izquierdo.
            nodo.izquierdo = self._insertar(nodo.izquierdo, jugador, puntaje)
        
        elif puntaje > nodo.puntaje: # Si el puntaje es mayor, intenta insertar en el subárbol derecho.
            nodo.derecho = self._insertar(nodo.derecho, jugador, puntaje)
        
        return nodo # No hace nada si el puntaje ya existe.


    def inorden(self): # Devuelve una lista de tuplas en orden ascendente de puntaje.
        resultado = []
        self._inorden(self.raiz, resultado) # Usa esta funcion para recorrer el árbol.
        return resultado


    def _inorden(self, nodo, res): # Recorre el árbol en orden: izquierdo, nodo, derecho.
        if nodo:
            self._inorden(nodo.izquierdo, res)
            res.append((nodo.jugador, nodo.puntaje)) # Añade cada jugador y puntaje a la lista.
            self._inorden(nodo.derecho, res)


    def buscar(self, puntaje): # Busca un jugador por su puntaje.
        return self._buscar(self.raiz, puntaje) # Devuelve el nombre y puntaje si lo encuentra. Si no lo encuentra, devuelve un mensaje "mensaje no encontrado".


    def _buscar(self, nodo, puntaje): # Recorre el árbol recursivamente.
        if nodo is None: # Si el nodo es None, no encontro nada.
            return "Jugador no encontrado"
        
        if puntaje == nodo.puntaje: # Si el puntaje es igual, devuelve el nodo.
            return nodo.jugador, nodo.puntaje
    
        if puntaje < nodo.puntaje: # Si es menor, busca a la izquierda.
            return self._buscar(nodo.izquierdo, puntaje)
        
        return self._buscar(nodo.derecho, puntaje) # Si es mayor, busca a la derecha.


    def eliminar(self, puntaje): # Elimina un jugador del árbol según su puntaje.
        self.raiz = self._eliminar(self.raiz, puntaje) # Usa esta funcion para ajustar el árbol recursivamente.


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
            # Encontré el nodo aquí van los 3 casos

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

    # Devuelve el nodo con menor puntaje en el subárbol dado, siguiendo siempre a la izquierda.
    def _minimo(self, nodo):
        while nodo.izquierdo is not None:
            nodo = nodo.izquierdo
        return nodo