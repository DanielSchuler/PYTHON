
from UsuarioDAO import UsuarioDAO
from logger_base import log
from Usuario import Usuario
import sys

contador=0
while contador != 5:
    seleccion=int(input('''Escriba el numero de de la opcion que deseas consultar
    1) Listar Usuarios
    2) Agreagar Usuario
    3) Modificar Usuario
    4) Eliminar Usuario
    5) Salir del programa'''))


    if seleccion==1:

        usuarios=UsuarioDAO.seleccionar()
        for usuario in usuarios:
            log.info(usuario)
    elif seleccion==2:

        user_name=input('Escriba el nombre de usuario')
        password=input('escriba el password del usuario')

        usuario= Usuario(nUser=user_name,nPassword=password)
        usuario_insertar=UsuarioDAO.insertar(usuario)

        log.info(f'usuario insertado: {usuario_insertar}')
    elif seleccion ==3:
        identificador=int(input('escriba el id del usuario que quiere modificar'))
        nusuario=input('escriba cual es el nuevo nombre del usuario')
        npassword=input('escriba el nuevo password')

        usuario = Usuario(identificador,nusuario, npassword)
        usuario_actualizardo=UsuarioDAO.actualizar(usuario)
        log.info(f'usuario actualizado: {usuario_actualizardo}')

    elif seleccion==4:
        identificador=int(input('escriba el identificador del usuario a eliminar'))
        usuario=Usuario(nId=identificador)
        usuario_eliminar=UsuarioDAO.eliminar(usuario)
        log.info(f'usuario eliminado: {usuario_eliminar}')

    elif seleccion == 5:
        log.info('gracias por sus servicios')
        sys.exit()










