from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
    #   print(objeto)
    print(type(objeto))
    print(objeto.mostrar_detalles())

    #si quiero acceder a un atributo que le pertenece a un hijo  y no al padre
    #y se quiere evitar el error porque ese atributo no existe
    #se pregunta si es una instancia

    if isinstance(objeto,Gerente):
        print(objeto.departamento)

empleado1=Empleado('Juan',5000)
imprimir_detalle(empleado1)

gerente = Gerente('Daniel',7000,'Sistemas')
imprimir_detalle(gerente)