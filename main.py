from cola import Queue, Jugador
from pila import Stack, Partida
from bst import BST

def cargar_datos_iniciales(cola, pila, bst):
    jugadores = [
        Jugador("Juan Perez", "JuanPro", 100),
        Jugador("Ana Gabriel", "AnaGamer", 75),
        Jugador("Alexis", "AlexElPro", 200),
        Jugador("Abelardo de la aspriella", "Abelardo", 50),
        Jugador("Vicente Fernandez", "ElCaballo", 500)
        ]
    
    for jugador in jugadores:
        cola.encolar(jugador)
        bst.insertar(jugador.alias, jugador.puntaje)

    print("5 jugadores cargados correctamente.")

def mostrar_menu():
    print("\n"+"<"+"-"*20+"Bienvenido a PixelArena"+"-"*20+">"+"\n")
    print("<-¡Preparado para comenzar el juego!->\n")
    print("---Lista de comandos---\n1) Ingresar jugador\n2) Llama al siguiente jugador\n3) Ver proximo jugador\n4) Registrar resultado de partida\n5) Deshacer el ultimo resultado\n6) Ver historial de partidas\n7) Insertar jugador en el ranking\n8) Buscar jugador por puntaje\n9) Mostrar ranking completo\n10) Eliminar jugador del ranking\n0) Salir\n")

def main():
    cola = Queue()
    pila = Stack()
    bst = BST()

    cargar_datos_iniciales(cola, pila, bst)

    while True:
        mostrar_menu()
        opcion = input("Seleccionar una opcion: ")

        if opcion == "0":
            print("Hasta luego")
            break

        elif opcion == "1":
            nombre = input("Ingresa tu nombre: ")
            apodo = input("Ingresa tu apodo: ")
            puntaje = int(input("Ingresa tu puntaje: "))
            cola.encolar(Jugador(nombre, apodo, puntaje))

        elif opcion == "2":
            cola.desencolar()

        elif opcion == "3":
            print(cola.ver_primero())
        
        elif opcion == "4":
            ganador = input("Ingresar alias del ganador: ")
            perdedor = input("Ingresar alias del perdedor: ")
            puntaje = int(input("Ingresar el puntaje de la partida: "))
            pila.apilar(Partida(ganador, perdedor, puntaje))

        elif opcion == "5":
            pila.desapilar()
        
        elif opcion == "6":
            pila.mostrar_historial()

        elif opcion == "7":
            jugador = input("Ingresar alias del jugador: ")
            puntaje = int(input("Ingresar puntaje del jugador: "))
            bst.insertar(jugador, puntaje)

        elif opcion == "8":
            puntaje = int(input("Ingresar puntaje de jugador: "))
            print(bst.buscar(puntaje))

        elif opcion == "9":
            orden_lista = bst.inorden()
            for i, (jugador, puntaje) in enumerate(orden_lista, 1):
                print(f"{i}, {jugador} -> {puntaje} pts.")

        elif opcion == "10":
            puntaje = int(input("Ingresar puntaje de jugador a eliminar: "))
            bst.eliminar(puntaje)


if __name__ == "__main__":
    main()