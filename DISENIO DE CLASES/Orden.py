from Producto import Producto

class Orden:

    contador_orden=0

    @classmethod
    def __siguiente_contador_orden(cls):
        cls.contador_orden+=1
        return cls.contador_orden

    def __init__(self,nPrductos):
        self.__id=Orden.__siguiente_contador_orden()
        # mejora al codigo hacer el casteo... si no es una lista genera un error
        self.__productos=list(nPrductos)

    @property
    def productos(self):
        return self.__productos

    @property
    def id(self):
        return self.__id

    def agregar_productos(self,nProducto):
        self.productos.append(nProducto)

    def calcular_total(self):
        total=0
        for producto in self.productos:
            total+=producto.precio
        return total


    def __str__(self):
        productos_str=''
        for producto in self.productos:
            productos_str += producto.__str__() +'|'+'\n'



        return f'''
        La orden tiene la siguiente informacion
        id:{self.id}
        {productos_str}
         '''

if __name__ == '__main__':
    producto1=Producto('camisa',100.00)
    print(producto1)

    producto2 = Producto('pantalon', 150.00)
    print(producto2 )


    lista_productos=[producto1,producto2]

    la_orden=Orden(lista_productos)
    print('se imprime la lista de productos'.center(50,'-'))
    print(la_orden)