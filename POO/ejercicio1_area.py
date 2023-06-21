class Cuadrado():

    def __init__(self):
        self.base=0
        self.altura=0
    def set_base(self,nBase):
        self.base=nBase
    def set_altura(self,nAltura):
        self.altura=nAltura
    def get_altura(self):
        return self.altura
    def get_base(self):
        return self.base
    def get_area(self):
        area=self.base*self.altura
        return area


cuadrado1=Cuadrado()
cuadrado1.set_base(int(input('defina la base: ')))
cuadrado1.set_altura(int(input('defina la altura: ')))
print(f'la base especificada es {cuadrado1.get_base()}')
print(f'la altura especificada es {cuadrado1.get_altura()}')
print(f'el area resultante del cuadrado con base = {cuadrado1.get_base()} y altura = {cuadrado1.get_altura()} es {cuadrado1.get_area()}')

