from SERVICIO.CatalogoPeliculas import CatalogoPeliculas
from DOMINIO.Pelicula import Pelicula


catalogo=CatalogoPeliculas()
contador=0
while contador!=4:
    eleccion=0
    try:
        eleccion=int(input('''
                            seleccione una de las siguientes 4 opciones:
                            1. agregar una película a la lista
                            2. ver la lista de películas
                            3. eliminar la lista de películas
                            4. salir del programa
                            '''))
    except Exception as e:
        print('solo puede usar numeros para las elecciones')

    if eleccion==1:
        nombre=str(input('Escriba el nombre de la pelicula que quiere agregar a la lista'))
        pelicula=Pelicula(nombre)

        catalogo.agregar_pelicula(pelicula)
        print('Se agrego la pelicula')
        contador=1
    elif eleccion==2:
        catalogo.listar_peliculas()
        print('fin de la lista de peliculas')
        contador=2
    elif eleccion==3:
        try:
            catalogo.eliminar_lista()
            print('Se elimino la lista de peliculas')
        except Exception as e:
            print('la lista de peliculas ya habia sido eliminada')
        contador=3
    elif eleccion==4:
        print('Gracias por colaborar')
        contador=4
