# ==========================================================
# pila.py = Este es el historial de partidas en una clase pila(Stack)
# Sistema de Gestion de Torneos - PixelArena S.A.S.
# Estructura: Pila usa el principio(LIFO - Last In, First Out)
# ya que el ultimo resultado registrado es el primero en deshacerse
# ==========================================================

# Crea un registro de partida con alias de ganador, alias de perdedor y puntaje de la partida.
class Partida:
    def __init__(self, ganador, perdedor, puntaje):
        self.ganador = ganador
        self.perdedor = perdedor
        self.puntaje = puntaje

    # Devuelve una cadena con los datos de la partida para mostrarla.
    def __str__(self):
        return f"Ganador: {self.ganador}, Perdedor: {self.perdedor}, Puntaje: {self.puntaje}"

class Stack:
    def __init__(self):
    # Inicializa la pila con una lista vacia.
        self._datos = [] 


    # Esta funcion devuelve True si no hay partidas registradas, False si hay al menos una.
    def esta_vacia(self):
        return len(self._datos) == 0


    # La funcion 'apilar' agrega una partida al final de la pila.
    # Imprime que la partida fue registrada.
    def apilar(self, partida):
        self._datos.append(partida)
        print(f"Partida registrada: {partida}")


    # La funcion 'desapilar' quita la ultima partida registrada, si la pila está vacía, imprime que no hya partidas para deshacer y devuelve None.
    # Si hay una partida, la elimina, la imprime como deshecha y la devuelve.
    def desapilar(self):
        if self.esta_vacia():
            print("no hay partidas registradas para deshacer.")
            return None
        partida = self._datos.pop()
        print(f"Partida deshecha: {partida}")
        return partida


    # Esta funcion devuelve la partida más reciente sin eliminarla, si no hay nada, imprime un mensaje y devuelve None.
    def ver_tope(self):
        if self.esta_vacia():
            print("No hay partidas registradas.")
            return None
        return self._datos[-1]
    

    # La funcion 'mostrar_historial' muestra todas las partidas registradas en orden inverso.
    # Si no hay partidas, imprime que el historial está vacío.
    def mostrar_historial(self):
        if self.esta_vacia():
            print("El historial de partidas esta vacio.")
            return
        print("\n===== HISTORIAL DE PARTIDAS =====")
        [print(f"- {p}") for p in reversed(self._datos)]
        print("=================================")

