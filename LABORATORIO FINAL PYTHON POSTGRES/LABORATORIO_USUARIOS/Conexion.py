from psycopg2 import pool
from logger_base import log
import sys


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = '1234'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'

    _MIN_CON = 1
    _MAX_CON = 5

    _pool = None

    @classmethod
    def obtenerPool(cls):
        # si el pool de conexiones no existe se creda el pool
        if cls._pool is None:
            # se hace la conexión a la BD
            try:
                cls._pool = pool.SimpleConnectionPool(
                    cls._MIN_CON,
                    cls._MAX_CON,
                    user=cls._USERNAME,
                    password=cls._PASSWORD,
                    host=cls._HOST,
                    port=cls._DB_PORT,
                    database=cls._DATABASE
                )
                log.debug(f'Conexión exitosa {cls._pool}')
                return cls._pool
            # si ubo un error al momento de hacer la conexión
            except Exception as e:
                log.error(f'Ocurrio un error al obtener la conexión con la BD {e}')
                sys.exit()
        # si ya se tenia una conexión iniciada se devuelve la conexión
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        # Ya no manejamos una variable de clase sino una variable
        # local a este metodo
        # el pool tiene un metodo de obtener conexion llamada
        # getconn() que devuelve una conexion a base de datos

        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexión obtenida del pool de conexiones: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, nConexion):
        cls.obtenerPool().putconn(nConexion)
        log.debug(f'Regresamos la conexión de regreso al pool')

    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
