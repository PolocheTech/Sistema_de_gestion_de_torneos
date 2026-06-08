# Crea un jugador con nombre real, el apodo y su puntaje.
class Jugador():
    def __init__(self, jugador, alias, puntaje):
        self.jugador = jugador
        self.alias = alias
        self.puntaje = puntaje

    def __str__(self):
        return f"{self.jugador} | {self.alias} | {self.puntaje} pts"
    
class Queue():
    # Inicializa la cola con una lista vacia.
    def __init__(self):
        self._elementos = []


    # Agrega un jugador al final de la cola.
    def encolar(self, jugador):
        self._elementos.append(jugador)

        print(f"El {jugador.alias} fue agregado a la cola de espera.")


    # La funcion 'desencolar' saca el primer jugador de la cola, si la cola está vacía, devuelve un mensaje de error.
    # Muestra quién es llamado al juego y devuelve al jugador que se sacó.
    def desencolar(self):
        if len(self._elementos) == 0:
            return "La cola esta vacia."
        
        jugador = self._elementos.pop(0)
        print(f"{jugador.alias} es llamado al juego.")
        return jugador
    

    # La funcion 'esta_vacia' devuelve True si no hay jugadores en la cola, False si hay al menos uno.
    def esta_vacia(self):
        return len(self._elementos) == 0
    

    # La funcion 'ver_primero' devuelve el primer jugador de la cola sin sacarlo, si la cola está vacía, devuelve un mensaje diciendo que está vacía.
    def ver_primero(self):
        if self.esta_vacia():
            return "La cola esta vacia."
        
        return self._elementos[0]


    # Esta ultima funcion imprime la lista de jugadores en espera con su posicion, si la cola está vacía, muestra un mensaje indicando eso.
    def mostrar_cola(self):
        if self.esta_vacia():
            return "La cola de espera esta vacia."
        
        print("\n---- Cola de espera ----\n")
        for i, jugador in enumerate(self._elementos):
            print(f"El jugador {jugador} esta en la posicion {i + 1}")
        print("\n--------------------------------")