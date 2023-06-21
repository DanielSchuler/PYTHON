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

# generacion de un cursor que permite hacer sentencias SQL de Python a Postgresql

cursor=conexion.cursor()
sentencia= 'SELECT * FROM persona'
cursor.execute(sentencia)

# generamos la variable registro para almacenar todos los registros

registros= cursor.fetchall()
# es una lista de todos los registros de nuestra tabla
# es una lista pero internamente es una tupla

print(registros)

# finalmente se cierran las conecciones

cursor.close()
conexion.close()