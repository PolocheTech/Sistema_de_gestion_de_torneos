# ==========================================================
# pila.py = Este es el historial de partidas en una clase pila(Stack)
# Sistema de Gestion de Torneos - PixelArena S.A.S.
# Estructura: Pila usa el principio(LIFO - Last In, First Out)
# ya que el ultimo resultado registrado es el primero en deshacerse
# ==========================================================

class Partida:
    def __init__(self, ganador, perdedor, puntaje):
        self.ganador = ganador
        self.perdedor = perdedor
        self.puntaje = puntaje

    def __str__(self):
        return f"Ganador: {self.ganador}, Perdedor: {self.perdedor}, Puntaje: {self.puntaje}"

class Stack:
    def __init__(self):
        self._datos = []

    def esta_vacia(self):
        return len(self._datos) == 0

    def apilar(self, partida):
        self._datos.append(partida)
        print(f"Partida registrada: {partida}")

    def desapilar(self):
        if self.esta_vacia():
            print("no hay partidas registradas para deshacer.")
            return None
        partida = self._datos.pop()
        print(f"Partida deshecha: {partida}")
        return partida

    def ver_tope(self):
        if self.esta_vacia():
            print("No hay partidas registradas.")
            return None
        return self._datos[-1]

    def mostrar_historial(self):
        if self.esta_vacia():
            print("el historial de partidas esta vacio")
            return
        print("\n===== HISTORIAL DE PARTIDAS =====")
        for i, partida in enumerate(reversed(self._datos), 1):
            print(f"{i}. {partida}")
        print("=================================")

