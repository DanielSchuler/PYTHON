import psycopg2 as bd
from logger_base import log

import sys
class Conexion:
    _DATABASE='test_db'
    _USERNAME='postgres'
    _PASSWORD='1234'
    _DB_PORT='5432'
    _HOST='127.0.0.1'

    _conexion=None
    _cursor =None

    @classmethod
    def obtenerConexion(cls):
        #primero preguntamos si el objeto coneccion no existe entonces hacemos una
        if cls._conexion is None:
            try:
                cls._conexion = bd.connect(
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Coneccion exitosa {cls._conexion}')
                return cls._conexion

            except Exception as e:
                # se usa mejor el log.error porque es un error de nuestra aplicacion
                log.error(f'Ocurrio el error al obtener la conexión {e}')
                sys.exit()

        else:
            # si el objeto coneccion ya existe devolvemos esa coneccion
            return cls._conexion


    @classmethod
    def obtenerCursor(cls):
        # preguntamos si no hay un cursor y si no entonces creamos uno

        if cls._cursor is None:
            # Para crear el cursor usamos try except
            try:
                cls._cursor=cls.obtenerConexion().cursor()
                log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                #log.debug()
                # se puede usar mejor log.error porque es un error de coneccion a base de datos
                log.error(f'Ocurrio una excepcion al obtener el cursor {e}')
                sys.exit()

        else:
            # si ya existe el cursor devolvemos el cursor existente
            return cls._cursor



if __name__ == '__main__':

    # probamos la conexion
    Conexion.obtenerConexion()
    #Probamos el cursor
    Conexion.obtenerCursor()