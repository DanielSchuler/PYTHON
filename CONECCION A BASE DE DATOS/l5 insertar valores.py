

# cuando se abre un objeto coneccion aunque se use el with se debe cerrar la coneccion manualmente
import psycopg2

# generando la coneccion
# el ultimo parametro para poder conectar es un **kwargs que permite mandar un diccionario de valores
conexion = psycopg2.connect(
    user='postgres',
    password='1234',
    host='127.0.0.1',
    port='5432',
    database='test_db'
)

try:
    with conexion:
        # generacion de un cursor que permite hacer sentencias SQL de Python a Postgresql

        with conexion.cursor() as cursor:


            #sentencia= 'SELECT * FROM persona'

            # se puede especificar las columnas que se desea extraer
            #sentencia = 'SELECT id_persona,nombre FROM persona'

            # se puede especificar los registros que se desean extraer
            #sentencia = 'SELECT nombre,email FROM persona WHERE id_persona=1'

            # si deseamos pasar un parametro usamos %s
            #sentencia = 'SELECT nombre,email FROM persona WHERE id_persona=%s'

            #si se desea usar codigo duro para extraer varios registros pero se debe usar el fetch all
            #sentencia = 'SELECT nombre,email FROM persona WHERE id_persona IN (1,2,3)'
            #cursor.execute(sentencia)

            # si queremos que la sentencia sea dinamica usamos %s

            sentencia = 'INSTERT INTO  persona (nombre,apellido,email) value(%s,%s,%s)'
            # necesito una tupla de tuplas
            valores = (('calros','lara','la@gmail.com'),)
            cursor.execute(sentencia,valores)
            # con commmit podemos guardarl los datos en la BD
            conexion.commit()
            # si queremos saber cuantos registros fueron insertados
            registros_insertados= cursor.rowcount
            print(f'Registros insertados {registros_insertados}')
except Exception as e:
    print( f'Ocurrio un error {e}')

finally:
    # finalmente se cierran las conecciones


    conexion.close()