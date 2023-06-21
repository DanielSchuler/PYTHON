from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):


    contadorTeclados=0

    @classmethod
    def siguiente_contador(cls):
        cls.contadorTeclados+=1
        return cls.contadorTeclados

    def __init__(self,nTipoEntrada,nMarca):
        DispositivoEntrada.__init__(self,nTipoEntrada,nMarca)
        self.__id=self.siguiente_contador()

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f'Id: {self.id},Teclado:{DispositivoEntrada.__str__(self)}'

if __name__ == '__main__':
    obj1_teclado=Teclado('USB','Toshiba')

    print('se crea el objeto 1 de tipo teclado'.center(50,'-'))
    print(obj1_teclado)

    obj2_teclado = Teclado('USB', 'Microsoft')

    print('se crea el objeto 2 de tipo teclado'.center(50, '-'))
    print(obj2_teclado)