from logger_base import log
from Conexion import Conexion


class CursorDelPool:

    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    @property
    def conexion(self):
        return self.__conexion

    @conexion.setter
    def conexion(self, nConexion):
        self.__conexion = nConexion

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, nCursor):
        self.__cursor = nCursor

    def __enter__(self):
        # este metodo se encarga de obtener una conexion
        log.debug('Inicio del método with __enter__')
        self.conexion = Conexion.obtenerConexion()
        self.cursor = self.conexion.cursor()
        return self.cursor

    # metodo exit hace commit o rollback de la transaccion y de regresar el objeto
    # conexion de regreso al pool
    def __exit__(self, tipo_exepcion, valor_exepcion, detalle_exepcion):
        log.debug('Se ejecuta el método __exit__')
        if valor_exepcion:
            self.conexion.rollback()
            log.error(f'Ocurrio una exepción, se hace rollback: {valor_exepcion}, {tipo_exepcion}, {detalle_exepcion}')
        else:
            self.conexion.commit()
            log.debug('Commit de la transacción')

        self.cursor.close()
        Conexion.liberarConexion(self.conexion)