

class Orden:

    contadorOrden=0

    @classmethod
    def siguiente_contador(cls):
        cls.contadorOrden+=1
        return cls.contadorOrden

    def __init__(self,nComputadoras):
        self.__id=self.siguiente_contador()
        self.__computadoras=list(nComputadoras)

    @property
    def id(self):
        return self.__id
    @property
    def computadoras(self):
        return self.__computadoras

    def agreagar_computadora(self,nComputadora):
        self.computadoras.append(nComputadora)

    def __str__(self):
        productos_str=''

        for computadora in self.computadoras:
            productos_str+=computadora.__str__() + '|'+ '\n'
        return  productos_str