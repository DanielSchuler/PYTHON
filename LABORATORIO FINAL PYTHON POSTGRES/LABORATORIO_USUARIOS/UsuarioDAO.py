from logger_base import log
from Cursor_del_pool import CursorDelPool

from Usuario import Usuario


class UsuarioDAO:

    # Creacion de sentencias SQL
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(usuario,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE usuario SET usuario=%s,password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'


    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECCIONAR)
            registros=cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario=Usuario(registro[0],registro[1],registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls,nUsuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario a insertar {nUsuario}')
            # tupla de valores a insertar

            valores=(nUsuario.user,nUsuario.password)



            cursor.execute(cls._INSERTAR,valores)

            return cursor.rowcount

    @classmethod
    def actualizar(cls,nUsuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario actualizado: {nUsuario}')
            valores=(nUsuario.user,nUsuario.password,nUsuario.id)
            # ejecutamos la sentencia SQL y pasamos la tupla de valores
            cursor.execute(cls._ACTUALIZAR,valores)

            return cursor.rowcount


    @classmethod
    def eliminar(cls,nUsuario):
        with CursorDelPool() as cursor:
            log.debug(f'Usuario eliminado: {nUsuario}')
            valores=(nUsuario.id,)
            cursor.execute(cls._ELIMINAR,valores)

            return cursor.rowcount


if __name__ == '__main__':

    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)