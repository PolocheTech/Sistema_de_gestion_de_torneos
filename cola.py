class Jugador():
    def __init__(self, jugador, alias, puntaje):
        self.jugador = jugador
        self.alias = alias
        self.puntaje = puntaje

    def __str__(self):
        return f"{self.jugador} | {self.alias} | {self.puntaje} pts"
    
class Queue():
    def __init__(self):
        self._elementos = []

    def encolar(self, jugador):
        self._elementos.append(jugador)

        print(f"El {jugador.alias} fue agregado a la cola de espera.")

    def desencolar(self):
        if len(self._elementos) == 0:
            return "La cola esta vacia."
        
        jugador = self._elementos.pop(0)
        print(f"{jugador.alias} es llamado al juego.")
        return jugador
    
    def esta_vacia(self):
        return len(self._elementos) == 0
    
    def ver_primero(self):
        if self.esta_vacia():
            return "La cola esta vacia."
        
        return self._elementos[0]

    def mostrar_cola(self):
        if self.esta_vacia():
            return "La cola de espera esta vacia."
        
        print("\n---- Cola de espera ----\n")
        for i, jugador in enumerate(self._elementos):
            print(f"El jugador {jugador} esta en la posicion {i + 1}")
        print("\n--------------------------------")