
class FiguraGeometrica():
    def __init__(self,nAlto,nAncho):
        #validacion de datos
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
        #self.__alto = nAlto
        #self.__ancho = nAncho
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
        #self.__ancho=nAncho
        if self.__validar_valor(nAncho):
            self.__ancho = nAncho
        else:
            print(f'valor invalido para {nAncho}')
            self.__ancho = 0

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