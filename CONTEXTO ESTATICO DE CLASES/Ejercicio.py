
# Para cada objeto de tipo persona vamos a crear un identificador unico
# por medio de una variable de clase vamos a generar un identificador para cada objeto de tipo persona
class Persona():
    contador_personas=0

    #mejora al ejercicio contador_personas
    @classmethod
    def generar_sigueinte_valor(cls):
        cls.contador_personas+=1
        return cls.contador_personas

    def __init__(self, nNombre,nEdad):

        #para incrementar valor de un atributo de clase se llama a la clase y luego a la variable
        #Persona.contador_personas+=1
        #self.__id_persona = Persona.contador_personas

        self.__id_persona = Persona.generar_sigueinte_valor()
        self.__nombre=nNombre
        self.__edad=nEdad
    @property
    def id(self):
        return self.__id_persona
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad
    def __str__(self):
        return f'Persona con los valores [id: {self.id}, nombre:{self.nombre},edad:{self.edad} ]'


# se crean los objetos

print('objeto 1'.center(50,'-'))

persona1 = Persona('Daniel',35)
print(persona1.__str__())

print('objeto 2'.center(50,'-'))

persona2 = Persona('Philipp',34)
print(persona2.__str__())