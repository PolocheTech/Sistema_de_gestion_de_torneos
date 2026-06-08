# Sistema de Gestión de Torneos

Este proyecto implementa un sistema de gestión de torneos de videojuegos en Python usando estructuras de datos básicas: colas, pilas y árboles binarios de búsqueda (BST).

## Descripción

El sistema permite:
- Registrar jugadores y agregarlos a una cola de espera.
- Llamar al siguiente jugador para iniciar una partida.
- Registrar resultados de partidas en una pila para poder deshacer el último resultado.
- Mantener un ranking de jugadores usando un árbol binario de búsqueda ordenado por puntaje.
- Buscar jugadores por puntaje y eliminar jugadores del ranking.

## Estructuras implementadas

- `Queue` en `cola.py`: representa una cola FIFO para el manejo de la lista de espera.
- `Stack` en `pila.py`: representa una pila LIFO para el historial de partidas y la función de deshacer.
- `BST` en `bst.py`: representa un árbol binario de búsqueda para organizar el ranking de jugadores por puntaje.

## Archivos principales

- `main.py`: controla el flujo del programa y el menú interactivo.
- `cola.py`: define las clases `Jugador` y `Queue`.
- `pila.py`: define las clases `Partida` y `Stack`.
- `bst.py`: define el árbol binario de búsqueda y sus operaciones.

## Uso

1. Ejecutar el archivo principal:
   ```bash
   python main.py
   ```
2. Elegir una opción del menú para:
   - ingresar jugadores,
   - llamar al próximo en cola,
   - registrar partidas,
   - deshacer resultados,
   - ver historial,
   - administrar el ranking.

## Requisitos

- Python 3.x

## Notas

Este proyecto se enfoca en el uso de estructuras de datos y su aplicación en un sistema sencillo de gestión de torneo. Para un proyecto más completo, se puede extender con persistencia de datos, validaciones adicionales y una interfaz gráfica o web.
