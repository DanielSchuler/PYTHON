


import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

# SI EL AUTO COMMIT ES IGUAL A TRUE NO SE TIENE QUE HACER COMMIT NI ROLLBACK
# No es buena practica y se debe hacer commit de manera manual para tener mas control
# esto se usa mucho en los test o manejo de errores

try:
    # VAMOS A MANEJARL DE MANERA MANUAL
    # el auto commit permite que se envien datos de manera automatica sin una segunda instancia
    # LO PONDREMOS EN FALSO y significa que si no hacemos commit al final no se ejecutan los cambios
    conexion.autocommit=False
    cursor= conexion.cursor()
    sentencia= 'INSERT INTO persona(nombre,apellido,email) VALUES (s%,s%,s%)'
    valores=('Maria','Esperanza','ma@gmail.com')
    cursor.execute(sentencia,valores)
    # si no agregamos esto no se ejecuta la transaccion se puede hacer el rollback en el exeption
    conexion.commit()
    print('termina la transaccion')

except Exception as e:

    # si hacemos el modo commit tambien podemos hacer el rollback
    conexion.rollback()
    print( f'Ocurrio un error se hizo rollback de la transaccion {e}')

finally:



    conexion.close()