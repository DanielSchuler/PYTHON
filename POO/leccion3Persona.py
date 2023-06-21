class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self,nNombre,nApellido,nEdad):

        #atributos de instancia
        self.nombre=nNombre
        self.apellido=nApellido
        self.edad=nEdad
#Creacion de mas de un objeto de la clase Persona
persona=Persona('Juan','Perez',10)
print(f'persona1 = {persona.nombre},{persona.apellido},{persona.edad}')


persona2=Persona('Karla','Gomez',15)
print(f'persona2 = {persona2.nombre},{persona2.apellido},{persona2.edad}')