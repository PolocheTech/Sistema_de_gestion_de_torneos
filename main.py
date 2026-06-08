from cola import Queue, Jugador
from pila import Stack, Partida
from bst import BST


# Se crean 5 jugadores iniciales con nombre, alias y su puntaje
def cargar_datos_iniciales(cola, pila, bst):
    jugadores = [
        Jugador("Juan Perez", "JuanPro", 100),
        Jugador("Ana Gabriel", "AnaGamer", 75),
        Jugador("Alexis", "AlexElPro", 200),
        Jugador("Abelardo de la aspriella", "Abelardo", 50),
        Jugador("Vicente Fernandez", "ElCaballo", 500)
        ]
    
    # Se agregan a la cola de espera y al árbol del ranking usando su alias y puntaje.
    for jugador in jugadores:
        cola.encolar(jugador)
        bst.insertar(jugador.alias, jugador.puntaje)

    # Imprime que los jugadores se cargaron correctamente.
    print("5 jugadores cargados correctamente.")


# Esta funcion 'mostrar_menu' imprime en pantalla el menú de opciones del sistema.
# Enumera las opciones del 1 al 10 y la opcion 0 para salir.
def mostrar_menu():
    print("\n"+"<"+"-"*20+"Bienvenido a PixelArena"+"-"*20+">"+"\n")
    print("<-¡Preparado para comenzar el juego!->\n")
    print("---Lista de comandos---\n1) Ingresar jugador\n2) Llama al siguiente jugador\n3) Ver proximo jugador\n4) Registrar resultado de partida\n5) Deshacer el ultimo resultado\n6) Ver historial de partidas\n7) Insertar jugador en el ranking\n8) Buscar jugador por puntaje\n9) Mostrar ranking completo\n10) Eliminar jugador del ranking\n0) Salir\n")


# En esta funcion principal 'main' se crean una instancia de la cola, la pila de partidas y el arbol BST.
# Se cargan los datos iniciales.
def main():
    cola = Queue()
    pila = Stack()
    bst = BST()

    cargar_datos_iniciales(cola, pila, bst)

    # Se ejecuta el bucle 'while True' que muestra el menú y espera la opción del usuario. 
    while True:
        mostrar_menu()
        opcion = input("Seleccionar una opcion: ")

        # Sale del programa.
        if opcion == "0":
            print("Hasta luego")
            break
        
        # Pide nombre, apodo y puntaje, agrega un nuevo jugador a la cola.
        elif opcion == "1":
            nombre = input("Ingresa tu nombre: ")
            apodo = input("Ingresa tu apodo: ")
            puntaje = int(input("Ingresa tu puntaje: "))
            cola.encolar(Jugador(nombre, apodo, puntaje))

        # Llama al siguiente jugador de la cola
        elif opcion == "2":
            cola.desencolar()

        # Muestra quien está primero en la cola sin sacarlo.
        elif opcion == "3":
            print(cola.ver_primero())
        
        # Pide alias del ganador, perdedor y puntaje, y registra una partida en la pila.
        elif opcion == "4":
            ganador = input("Ingresar alias del ganador: ")
            perdedor = input("Ingresar alias del perdedor: ")
            puntaje = int(input("Ingresar el puntaje de la partida: "))
            pila.apilar(Partida(ganador, perdedor, puntaje))

        # Deshace la ultima partida registrada.
        elif opcion == "5":
            pila.desapilar()
        
        # Muestra el historial de partidas.
        elif opcion == "6":
            pila.mostrar_historial()

        # Inserta un jugador nuevo en el ranking BST.
        elif opcion == "7":
            jugador = input("Ingresar alias del jugador: ")
            puntaje = int(input("Ingresar puntaje del jugador: "))
            bst.insertar(jugador, puntaje)

        # Busca un jugador por puntaje en el BST.
        elif opcion == "8":
            puntaje = int(input("Ingresar puntaje de jugador: "))
            print(bst.buscar(puntaje))

        # Muestra el ranking completo en orden ascendente de puntaje.
        elif opcion == "9":
            orden_lista = bst.inorden()
            for i, (jugador, puntaje) in enumerate(orden_lista, 1):
                print(f"{i}, {jugador} -> {puntaje} pts.")

        # Elimina un jugador del ranking por puntaje
        elif opcion == "10":
            puntaje = int(input("Ingresar puntaje de jugador a eliminar: "))
            bst.eliminar(puntaje)


if __name__ == "__main__":
    main()