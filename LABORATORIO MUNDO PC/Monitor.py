
class Monitor:

    contadorMonitor=0

    @classmethod
    def siguiente_contador(cls):
        cls.contadorMonitor+=1
        return cls.contadorMonitor

    def __init__(self,nMarca,nTamanio):
        self.__id=self.siguiente_contador()
        self.__marca=nMarca
        self.__tamanio=nTamanio
    @property
    def id(self):
        return self.__id

    @property
    def marca(self):
        return self.__marca

    @property
    def tamanio(self):
        return self.__tamanio
    def __str__(self):
        #f'Id: {self.id},Marca:{self.marca},Tipo Entrada: {self.tipoEntrada}'
        return f'Id: {self.id},Monitor[Marca: {self.marca},Tamanio:{self.tamanio}'
