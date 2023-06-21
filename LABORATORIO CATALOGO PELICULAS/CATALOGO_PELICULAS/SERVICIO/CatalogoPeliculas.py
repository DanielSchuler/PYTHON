import os
from .ManejoArchivos import ManejoArchivos

class CatalogoPeliculas:

    ruta_archivo='lista_peliculas.txt'

    #segun lo que explica el profesor quedo faltando usar metodos de clase class method para definir
    # el agregar pelicula
    # listar peliculas
    # eliminar peliculas

    @classmethod
    def agregar_pelicula(cls,pelicula):
        with ManejoArchivos(cls.ruta_archivo,'a') as archivo:
            archivo.write(pelicula.__str__()+'\n')
    @classmethod
    def listar_peliculas(cls):
        with ManejoArchivos(cls.ruta_archivo,'r') as archivo:
            # segun lo que el profesor escribio falto el titulo cuando sse lee la informacion
            print('Catalogo de películas'.center(50,'-'))
            # se corrigio de readline a read porque no estaba mostrando la info del documento
            print(archivo.read())

    @classmethod
    def eliminar_lista(cls):

        os.remove(cls.ruta_archivo)

