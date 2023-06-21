# SE GENERAN METODOS ABSTRACTOS EN FIGURA GEOMETRICA PARA QUE LAS CLASES HIJAS
# ESTEN OBLIGADAS A IMPLEMENTAR LOS METODOS
# PARA ESTO SE MODIFICARA LA CLASE PADRE PARA QUE SEA ABSTRACTA

# SE IMPORTA ABC= Abstract Base Class

from abc import ABC,abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,nAlto,nAncho):

        ''''''
        if self.__validar_valor(nAlto):
            self.__alto=nAlto
        else:
            print(f'valor invalido para {nAlto}')
            self.__alto=0
        if self.__validar_valor(nAncho):
            self.__ancho=nAncho
        else:
            print(f'valor invalido para {nAncho}')
            self.__ancho=0

    @property
    def alto(self):
        return self.__alto
    @alto.setter
    def alto(self,nAlto):
        #self.__alto=nAlto
        if self.__validar_valor(nAlto):
            self.__alto=nAlto
        else:
            print(f'valor invalido para {nAlto}')
            self.__alto=0

    @property
    def ancho(self):
        return self.__ancho
    @ancho.setter
    def ancho(self,nAncho):

        if self.__validar_valor(nAncho):
            self.__ancho = nAncho
        else:
            print(f'valor invalido para {nAncho}')
            self.__ancho = 0

    #Metodo abstracto
    @abstractmethod
    def area(self):
        pass
    def __str__(self):
        return f'las dimensiones de la figura geometrica, alto: {self.alto}, ancho: {self.ancho}'
    def __validar_valor(self,valor):
        return True if 0 <valor<10 else False
class Color():
    def __init__(self,nColor):
        self.__color=nColor
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,nColor):
        self.__color=nColor
    def __str__(self):
        return f'el color es: {self.color}'


class Cuadrado(FiguraGeometrica,Color):
    def __init__(self,nAlto,nAncho,nColor):
        FiguraGeometrica.__init__(self,nAlto,nAncho)
        Color.__init__(self,nColor)
        #self.__area=nAlto*nAncho

    @property
    def area(self):
        return f'el area calculada del Cuadrado da como resultado: {self.ancho*self.alto}'

    def __str__(self):
        return f'el area de la figura geometrica cuadrado es: {self.area} '+ FiguraGeometrica.__str__(self)+' '\
               + Color.__str__(self)


class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,nAlto,nAncho,nColor):
        FiguraGeometrica.__init__(self, nAlto, nAncho)
        Color.__init__(self, nColor)
        self.__area=nAlto*nAncho

    @property
    def area(self):
        return f'el area calculada del Rectangulo da como resultado: {self.__area}'

    def __str__(self):
        return f'el area de la figura geometrica rectangulo es: {self.area} '+ FiguraGeometrica.__str__(self)+' '\
               + Color.__str__(self)


if __name__ == '__main__':


    cuadrado1=Cuadrado(3,2,'Azul')
    print(cuadrado1)


    rectangulo=Rectangulo(4,2,'rojo')
    print(rectangulo)