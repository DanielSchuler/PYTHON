


respuesta=None

a=10
b=0


try:
    respuesta=a/b
# Esto si queremos ser más especificos lo que no es tan recomendable
except ZeroDivisionError as dz:
    print(f'ocmurrio un error2 {dz}')
except TypeError as tz:
    print(f'ocmurrio un error {tz}')
# este exept si queremos ser genericos lo que es mas recomendable... si se van a usar las
# si se van a usar las exepciones especificas la exepcion generica debe ir al final

except Exception as e:
    print(f'ocmurrio un error {e}')
else:
    # el bloque else permite mandar un mensaje si no ocurrio ninguna exepcion
    print('todo salio bien')


finally:
    print('me ejecuto si ocurre alguna exepcion o no ')



print(f'Resultado: {respuesta}')

print('continuamos...')