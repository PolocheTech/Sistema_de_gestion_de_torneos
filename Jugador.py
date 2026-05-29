class Entidad:

    def __init__(self,alias: str ):
        self.__alias = alias

    @property
    def alias(self) -> str:
        return self.__alias
    
    def describir(self) -> str:

        raise NotImplementedError("cada subclase deb implementar describir()")
    

    def __str__(self) -> str:
        return self.describir()
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(alias={self.__alias!r})"


    def __init__(self, nombre :str, alias: str, puntaje: int = 0):
        super().__init__(alias)
        self.__nombre = nombre
        self.__puntaje = max(0, puntaje)

    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def puntaje(self) -> int: 
        return self.__puntaje


    @puntaje.setter
    def puntaje(self, nuevo:int) ->None:
        if not isinstance(nuevo, int) or nuevo < 0:
            raise ValueError("El puntaje debe ser un entero no negativo.")
        self.__puntaje = nuevo

    def agregar_puntaje(self, puntos: int) ->None:
        if puntos < 0:
            raise ValueError("los puntos ah agregar no pueden ser negativos mi socio")
        self.__puntaje += puntos

    def describir(self) -> str:
        return(
            f"Jugador  Nombre: {self.__nombre:<20}"
            f"alias: {self.__alias:<15} "
            f"puntaje: {self.__puntaje:>6}"

        )


    def __eq__(self, otro) -> bool:
        return isinstance(otro, Jugador) and self.alias == otro.alias

    def __hash__(self):
        return hash(self.alias)
    
class Partida(Entidad):
    _contador: int = 0

    def __init__(self, alias_ganador: str, alias_perdedor: str, puntaje: int):
        super().__init__(alias_ganador)
        Partida._contador += 1
        self.__id_partida = Partida._contador
        self.__alias_perdedor = alias_perdedor
        self.__puntaje = max(0, puntaje)

    @property
    def id_partida(self) -> int:
        return self.__id_partida
    
    @property
    def alias_ganador(self) -> str:
        return self.alias    
        
    @property
    def alias_perdedor(self) -> str:
        return self.__alias_perdedor
 
    @property
    def puntaje(self) -> int:
        return self.__puntaje

    def describir(self) -> str:
        return (
            f"Partida #{self.__id_partida:03d} | "
            f"Ganador: {self.alias_ganador:<15} | "
            f"Perdedor: {self.__alias_perdedor:<15} | "
            f"Puntaje: {self.__puntaje:>6}"
        )