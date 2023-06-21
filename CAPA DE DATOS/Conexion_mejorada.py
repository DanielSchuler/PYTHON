
from logger_base import log
# con el pool de conexiones la importacion de la bd del psycopg2 no es requerida

#import psycopg2 as bd

# se manejara la importacion del pool de la libreria psycopg2
from psycopg2 import pool
import sys

# uso del pool de conexiones
# Hay un numero de conexiones en el pool. Cuando el usuario necesita hacer algo toma una conexion y cuando
# termina la devuelve al pool




class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='1234'
    _DB_PORT='5432'
    _HOST='127.0.0.1'

    # En el manejo del pool de conexiones los atributos de conexion y cursor no se manejara en esta clase

    #_conexion=None
    #_cursor =None

    # El pool de conexiones administrara las conexiones por eso requiere que se especifique un minimo y un
    # maximo de las conexiones
    _MIN_CON = 1
    # Este numero no puede ser muy grande porque las bases de datos tienen limites
    # Tener tantos objetos de conexion a una base de datos puede ser un proceso muy pesado
    # este numero se adecua dependiendo de las necesitades del proyecto
    _MAX_CON = 5
    # Se inicia el objeto pool como nulo
    _pool=None

    #1. Metodo para configurar el pool de conexiones

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                #inicializamos el pool
                #Forma mas sencilla de obtener las conexiones
                cls._pool =pool.SimpleConnectionPool(cls._MIN_CON,
                                                     cls._MAX_CON,
                                                     host=cls._HOST,
                                                     user=cls._USERNAME,
                                                     password=cls._PASSWORD,
                                                     port=cls._DB_PORT,
                                                     database=cls._DATABASE
                                                     )

                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool: {e}')
                sys.exit()

        # En caso de que el pool si exista lo devolvemos
        else:
            return cls._pool

    #2. Se modifica el metodo obtenerConexion simplificandola
    @classmethod
    def obtenerConexion(cls):
        # Ya no manejamos una variable de clase sino una variable local a este metodo
        # el pool tiene un metodo de obtener conexion llamada getconn() que devuelve una conexion a base de datos
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        # el objeto conexion la administrara otra clase
        return conexion

    #3. Ya tenemos como generar las conexiones ahora toca liberarlas
    @classmethod
    def liberarConexion(cls,nConexion):
        #llamamos al pool
        # para regresar el objeto de conexion de regreso al pool usamos putconn
        cls.obtenerPool().putconn(nConexion)
        log.debug(f'Regresamos la conexion de regreso al pool: {nConexion}')


    #4. Cerrar por completo  el pool de conexiones
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


    # El metodo def obtenerCursor(cls): no se manejara en esta clase por eso se borra
    # Se manejara desde otra clase que se dedicara a hacer esta tarea




if __name__ == '__main__':
    # validando los metodos de obtener conexion
    '''
    conexion1=Conexion.obtenerConexion()
    conexion2=Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()'''
    # si solicitamos una sexta conexion sin cerrar las anteriores se genera un error
    #conexion6 = Conexion.obtenerConexion()

    # simulacion de creacion y cierre de conexiones
    conexion1 = Conexion.obtenerConexion()
    Conexion.librerarConexion(conexion1)
    conexion2 = Conexion.obtenerConexion()