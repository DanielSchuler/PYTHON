class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self,nNombre,nApellido,nEdad):

        #atributos de instancia
        self.nombre=nNombre
        self.apellido=nApellido
        self.edad=nEdad
#se le mandan como parametros los valores a los atributos
persona=Persona('Juan','Perez',10)
print(persona.nombre)
print(persona.apellido)
print(persona.edad)