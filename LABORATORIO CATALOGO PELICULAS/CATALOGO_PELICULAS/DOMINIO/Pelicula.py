

class Pelicula:

    contador = 0

    @classmethod
    def siguiente_contador(cls):
        cls.contador+=1
        return cls.contador

    def __init__(self,nNombre):
        self.__id=Pelicula.siguiente_contador()
        self.__nombre=nNombre

    @property
    def nombre(self):
        return f'Nombre: {self.__nombre}'

    # como lo explica el profesor falta el setter

    @nombre.setter
    def nombre(self,nNombre):
        self.__nombre=nNombre

    @property
    def id(self):
        return f'Id: {self.__id}'

    def __str__(self):
        return f'Pelicula: [{self.id}, {self.nombre}] '


if __name__ == '__main__':
    print('test creacion peliculas'.center(50,'-'))
    pelicula1=Pelicula('batman')
    pelicula2 = Pelicula('superman')
    print('Resultado'.center(50,'-'))
    print(pelicula1)
    print(pelicula2)