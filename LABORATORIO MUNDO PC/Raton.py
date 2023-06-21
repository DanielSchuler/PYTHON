from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contadorRatones=0
    @classmethod
    def siguiente_contador(cls):
        cls.contadorRatones+=1
        return cls.contadorRatones

    def __init__(self,nTipoEntrada,nMarca):
        DispositivoEntrada.__init__(self,nTipoEntrada,nMarca)
        self.__id=self.siguiente_contador()
    @property
    def id(self):
        return self.__id



    def __str__(self):
        #f'Id: {self.id},Marca:{self.marca},Tipo Entrada: {self.tipoEntrada}'
        return f'Id: {self.id},Raton:{DispositivoEntrada.__str__(self)}'



if __name__ == '__main__':
    obj1_raton=Raton('USB','Toshiba')

    print('se crea el objeto 1 de tipo raton'.center(50,'-'))
    print(obj1_raton)

    obj2_raton = Raton('USB', 'Microsoft')

    print('se crea el objeto 2 de tipo raton'.center(50, '-'))
    print(obj2_raton)