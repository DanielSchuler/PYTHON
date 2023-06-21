
from LABORATORIO_USUARIOS.UsuarioDAO import UsuarioDAO


contador=0
while contador != 5:
    seleccion=int(input('''Escriba el numero de de la opcion que deseas consultar
    1) Listar Usuarios
    2) Agreagar Usuario
    3) Modificar Usuario
    4) Eliminar Usuario
    5) Salir del programa'''))


    if seleccion==1:

        print(UsuarioDAO.seleccionar())




