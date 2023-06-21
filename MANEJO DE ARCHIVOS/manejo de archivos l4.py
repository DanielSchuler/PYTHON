
# esta clase se puede usar tambien como ManejoRecursos
# para abrir coneccion a base de datos y cerrarla .. no solo a archivos
class ManejoArchivos:
    # se debe crear el metodo __enter_ y __exit__ que se conoce como context manager

    def __init__(self,nombre):
        self.nombre=nombre
    # este metodo se hereda de la clase object
    def __enter__(self):
        print('entramos al recurso'.center(50,'-'))
        self.nombre=open(self.nombre,'r',encoding='utf8')
        return self.nombre

    #def __exit__(self, exc_type, exc_val, exc_tb):
    # traza= lista de errores
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50,'-'))

        # si el archivo esta apuntando a un objeto ( esta abierto ) lo cerramos
        if self.nombre:
            self.nombre.close()


if __name__ == '__main__':


    with ManejoArchivos('prueba.txt') as archivo:
        print(archivo.read())

