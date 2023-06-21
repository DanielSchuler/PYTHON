from logger_base import log
from Conexion_mejorada import Conexion
class CursorDelPool:

    def __init__(self):
        self._conexion = None
        self._cursor = None

    def __enter__(self):
        # este metodo se encarga de obtener una conexion
        log.debug('Inicio del metodo with __enter__')
        self._conexion = Conexion.obtenerConexion()
        self._cursor = self._conexion.cursor()
        return self._cursor

    # metodo exit hace commit o rollback de la transaccion y de regresar el objeto
    # conexion de regreso al pool
    def __exit__(self, tipo_exepcion, valor_exepcion, detalle_exepcion):
        log.debug('Se ejecuta el metodo __exit__')
        if valor_exepcion:
            self._conexion.rollback()
            log.error(f'Ocurrio una exepcion, se hace rollback: {valor_exepcion}, {tipo_exepcion}, {detalle_exepcion}')
        else:
            self._conexion.commit()
            log.debug('Commit de la transaccion')

        self._cursor.close()
        Conexion.liberarConexion(self._conexion)


if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('Dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())