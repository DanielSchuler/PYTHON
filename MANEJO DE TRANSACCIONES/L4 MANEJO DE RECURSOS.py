
# PARA NO HACER EL COMMIT DE MANERA MANUAL PERO AUN ASI TENER CONTROL SE USA EL WITH

import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)


try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia= 'INSERT INTO persona(nombre,apellido,email) VALUES (s%,s%,s%)'
            valores=('Maria','Esperanza','ma@gmail.com')
            cursor.execute(sentencia,valores)

            sentencia= ' UPDATE persona SET nombre=%s, apellido=%s email=%s WHERE id_persona = 1'
            valores = ('Juan Carlos', 'Juares', 'jj@gmail.com')
            cursor.execute(sentencia, valores)



except Exception as e:

    # no se necesario usar el rollback porque se hace utomatico
    #conexion.rollback()
    print( f'Ocurrio un error se hizo rollback de la transaccion {e}')

finally:
    conexion.close()
# usamos esta linea al final para que se ejecute cuando termina la transaccion
    print('termina la transaccion')