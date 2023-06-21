


import psycopg2

conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)


try:

    #si quiero mas control pongo conexion.autocommit=False y pongo el rollback en el except
    # por defecto esta el autocommit =True
    cursor= conexion.cursor()
    sentencia= 'INSERT INTO persona(nombre,apellido,email) VALUES (s%,s%,s%)'
    valores=('Maria','Esperanza','ma@gmail.com')
    cursor.execute(sentencia,valores)

    sentencia= ' UPDATE persona SET nombre=%s, apellido=%s email=%s WHERE id_persona = 1'
    valores = ('Juan Carlos', 'Juares', 'jj@gmail.com')

    conexion.commit()
    print('termina la transaccion')

except Exception as e:

    # si hacemos el modo commit tambien podemos hacer el rollback
    #conexion.rollback()
    print( f'Ocurrio un error se hizo rollback de la transaccion {e}')

finally:



    conexion.close()