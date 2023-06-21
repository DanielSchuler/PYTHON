

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

            sentencia = 'SELECT nombre,email FROM persona WHERE id_persona IN %s'

            # debemos hacer una tupla de tuplas
            #llaves_primarias=((1,2,3),)

            # podemos pedirle al usuario la lista de llaves
            entradas =input('proporcione las llaves separadas por comas')
            llaves_primarias=(tuple(entradas.split(',')),)
            cursor.execute(sentencia,llaves_primarias)


            # generamos la variable registros para almacenar todos los registros
            registros= cursor.fetchall()

            # se puede procesar cada registro de manera independiente
            for registro in registros:
                print(registro)

            # es una lista de todos los registros de nuestra tabla
            # es una lista pero internamente es una tupla

            print(registros)
except Exception as e:
    print( f'Ocurrio un error {e}')

finally:
    # finalmente se cierran las conecciones


    conexion.close()