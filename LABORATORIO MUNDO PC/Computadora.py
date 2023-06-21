from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor

class Computadora:

    contadorComputadora=0

    @classmethod
    def siguiente_contador(cls):
        cls.contadorComputadora+=1
        return cls.contadorComputadora

    def __init__(self,nNombre,nMonitor,nTeclado,nRaton):

        self.__id=self.siguiente_contador()
        self.__nombre=nNombre
        self.__monitor=nMonitor
        self.__teclado=nTeclado
        self.__ratorn=nRaton


    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nNombre):
        self.__nombre=nNombre

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self,nMonitor):
        self.__monitor=nMonitor

    @property
    def teclado(self):
        return  self.__teclado

    @teclado.setter
    def teclado(self,nTeclado):
        self.__teclado=nTeclado

    @property
    def raton(self):
        return  self.__ratorn

    @raton.setter
    def raton(self,nRaton):
        self.__ratorn=nRaton


    def __str__(self):
        return f'''
{self.nombre}:{self.id}
Monitor: {self.monitor}
Teclado: {self.teclado}
Raton: {self.raton}
'''

if __name__ == '__main__':
    monitor1=Monitor('Asus',13)
    teclado=Teclado('integrado','Asus')
    raton=Raton('bluetooth','microsoft')
    print('se crea el objeto 1 de tipo teclado'.center(50, '-'))

    obj1_computadora=Computadora('Asus VivoBook 14/15',monitor1,teclado,raton)
    print(obj1_computadora)