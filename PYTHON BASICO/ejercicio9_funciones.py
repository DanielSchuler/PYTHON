def funcion_suma(*args):
    contador=0
    for e in args:
        if type(e)==int:
            contador+=e
        else:
            print('solo puedo sumar numeros')
    return contador

funcion_suma(1,2,3,'abc')