

class DispositivoEntrada:

    def __init__(self,nTipoEntrada,nMarca):
        self.__tipoEntrada=nTipoEntrada
        self.__marca=nMarca

    @property
    def tipoEntrada(self):
        return self.__tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self,nEntrada):
        self.__tipoEntrada=nEntrada

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self,nMarca):
        self.__marca=nMarca

    def __str__(self):
        return f'DispositivoEntrada: [TipoEntrada: {self.tipoEntrada}, Marca: {self.marca}]'




if __name__ == '__main__':
    obj1_dispositivoEntrada=DispositivoEntrada('nuevo','samsung')

    print('se imprime el objeto de tipo Entrada'.center(50,'-'))
    print(obj1_dispositivoEntrada)
