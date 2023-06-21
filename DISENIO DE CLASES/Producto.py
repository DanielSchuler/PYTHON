class Producto:
    contador_productos=0
    @classmethod
    def __siguiente_contador_producto(cls):
        cls.contador_productos+=1
        return cls.contador_productos

    def __init__(self,nNombre,nPrecio):
        self.__id=Producto.__siguiente_contador_producto()
        self.__nombre=nNombre
        self.__precio=nPrecio
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    def __str__(self):
        return f'producto: [id:{self.id},nombre:{self.nombre},precio:{self.precio}'



if __name__ == '__main__':
    producto1=Producto('camisa',100.00)
    print(producto1)

    producto2 = Producto('pantalon', 150.00)
    print(producto2 )