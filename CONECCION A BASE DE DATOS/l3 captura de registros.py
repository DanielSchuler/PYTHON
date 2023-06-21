

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
            sentencia = 'SELECT nombre,email FROM persona WHERE id_persona=%s'
            # se define el valor de la variable pero tener en cuenta que debe ser una tupla
            #id_persona = 1
            # se puede hacer aun mas dinamico. el %s permite que no tenga que ser castiado
            #id_persona = int(input('escriba el id que desea extraer'))
            id_persona = input('escriba el id que desea extraer')
            cursor.execute(sentencia,(id_persona,))

            # generamos la variable registro para almacenar todos los registros

            # conociendo que solo vamos a recibir un registro se puede optimizar el codigo solicitando
            # solo un registro
            #registros= cursor.fetchall()
            registros = cursor.fetchone()
            # es una lista de todos los registros de nuestra tabla
            # es una lista pero internamente es una tupla

            print(registros)
except Exception as e:
    print( f'Ocurrio un error {e}')

finally:
    # finalmente se cierran las conecciones


    conexion.close()