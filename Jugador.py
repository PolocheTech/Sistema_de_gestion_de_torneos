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




