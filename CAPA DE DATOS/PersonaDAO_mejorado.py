from logger_base import log

from Persona import Persona


from cursor_del_pool import CursorDelPool

class PersonaDAO:

    '''
    # DAO Data Acces Object
    # En esta clase se hace el CRUD Create Read Update Delete
    # parametros posicionales para definir las entradas %s
    '''
    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
    _ACTUALIZAR = 'UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):

        # como hemos creado el pool de conexiones haremos las siguientes modificaciones:
        #se elimina esta linea
        #with Conexion.obtenerConexion() as conexion:

        #Se corre el bloque de codigo con shift tab
        #Se modifica el objeto conexion por la clase CursorDelPool
        with CursorDelPool() as cursor:
            # con el cursor ya podemos ejecutar la sentecia SQL
            cursor.execute(cls._SELECCIONAR)
            # guardamos en la variable registros los datos capturados de la base de datos
            registros = cursor.fetchall()
            # no estamos obteniendo un objeto de tipo persona sino una lista
            # para ello vamos a guardar los objetos de tipo persona obtenido de los registros en una lista
            # de tipo persona
            personas = []
            for registro in registros:
                persona=Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls,nPersona):
        # como hemos creado el pool de conexiones haremos las siguientes modificaciones:
        # se elimina esta linea
        # with Conexion.obtenerConexion() as conexion:

        # Se corre el bloque de codigo con shift tab
        # Se modifica el objeto conexion por la clase CursorDelPool

        with CursorDelPool() as cursor:

            # con el cursor ya podemos ejecutar la sentecia SQL


            valores=(nPersona.nombre,nPersona.apellido,nPersona.email)
            # ejecutamos la sentencia SQL y pasamos la tupla de valores
            cursor.execute(cls._INSERTAR,valores)
            # Despues de ejecutar la sentencia SQL validamos en el log
            log.debug(f'Persona a insertar{nPersona}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls,nPersona):
        # como hemos creado el pool de conexiones haremos las siguientes modificaciones:
        # se elimina esta linea
        # with Conexion.obtenerConexion() as conexion:

        # Se corre el bloque de codigo con shift tab
        # Se modifica el objeto conexion por la clase CursorDelPool

        with CursorDelPool() as cursor:
            # con el cursor ya podemos ejecutar la sentecia SQL

            valores = (nPersona.nombre, nPersona.apellido, nPersona.email,nPersona.id)
            # ejecutamos la sentencia SQL y pasamos la tupla de valores
            cursor.execute(cls._ACTUALIZAR, valores)
            # Despues de ejecutar la sentencia SQL validamos en el log
            log.debug(f'Persona a actualizar{nPersona}')
            return cursor.rowcount

    @classmethod
    def eliminar(cls,nPersona):
        # como hemos creado el pool de conexiones haremos las siguientes modificaciones:
        # se elimina esta linea
        # with Conexion.obtenerConexion() as conexion:

        # Se corre el bloque de codigo con shift tab
        # Se modifica el objeto conexion por la clase CursorDelPool

        with CursorDelPool() as cursor:
            # con el cursor ya podemos ejecutar la sentecia SQL

            valores = (nPersona.id,)
            # ejecutamos la sentencia SQL y pasamos la tupla de valores
            cursor.execute(cls._ELIMINAR, valores)
            # Despues de ejecutar la sentencia SQL validamos en el log
            log.debug(f'Persona a eliminar{nPersona}')
            return cursor.rowcount


if __name__ == '__main__':

    # validar insercion
    # como el id es autogenerado toca especificar a que columnas vamos a insertar

    persona1 =Persona(nNombre='Alejandra',nApellido='Palacios',nEmail='apalacios@gmail.com')
    persona2 = Persona(nNombre='Tato',nApellido='Debia',nEmail='tdebia@gmail.com')
    persona_insertada=PersonaDAO.insertar(persona1)
    persona_insertada2=PersonaDAO.insertar(persona2)
    log.debug(f'personas insertadas: {persona_insertada}')
    log.debug(f'personas insertadas: {persona_insertada2}')
    ''''''

    #validar actualizacion
    # Como vamos a mandar todos los valores no necesito especificar los parametros
    # Si quiero cambiar el orden de entrada de los parametros si debo especificar el parametro
    '''
    persona1 = Persona(3,'Alejandro', 'Magno', nEmail='amagno@gmail.com')
    persona2 = Persona(nNombre='Shurima', nApellido='Amash', nEmail='samash@gmail.com',nId=4)


    # actualizamos
    persona_actualizada = PersonaDAO.actualizar(persona1)

    log.debug(f'personas actualizadas: {perona_actualizada}')
    persona_actualizada2 = PersonaDAO.actualizar(persona2)
    log.debug(f'personas actualizadas: {perona_actualizada2}')
    
    # Validar eliminacion
    # como solo se esta mandando un valor se debe especificar el nombre del parametro
    persona1 = Persona(nId=3)
    persona2 = Persona(nId=4)


    # eliminamos
    persona_eliminada = PersonaDAO.eliminar(persona1)

    log.debug(f'personas eliminadas: {persona_eliminada}')
    persona_eliminada2 = PersonaDAO.eliminar(persona2)
    log.debug(f'personas eliminadas: {persona_eliminada2}')
'''
    # validar seleccion
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)