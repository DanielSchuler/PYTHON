from logger_base import log


class Persona:

    def __init__(self, nId=None, nNombre=None, nApellido=None, nEmail=None):
        self.__id = nId
        self.__nombre = nNombre
        self.__apellido = nApellido
        self.__email = nEmail

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nId):
        self.__id = nId

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nNombre):
        self.__nombre = nNombre

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, nApellido):
        self.__apellido = nApellido

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nEmail):
        self.__email = nEmail

    def __str__(self):
        return f'''Se imprime el objeto persona con la siguiente información
        Persona: 
        Id:{self.id} ,
        Nombre: {self.nombre},
        Apellido:{self.apellido},
        Email: {self.email}'''


if __name__ == '__main__':
    persona1 = Persona(1, 'Daniel', 'Schuler', 'daniel.andreas87@gmail.com')

    # se usa el log para dar la informacion

    log.debug(persona1)
    print(persona1)

    # simular agregar un elemento
    # como el id no lo tengo que proporcionar... se ha asignado un valor de None por defecto
    # para que funcione se debe especificar que dato estoy introduciendo

    persona2 = Persona(nNombre='Juan', nApellido='ramirez', nEmail='jr@gmail.com')

    log.debug(persona2)
    print(persona2)
    # simular eliminar persona, solo se re quiere saber el id y poner todos los valores en none
    persona2 = Persona(nId=1)
    print(persona2)
