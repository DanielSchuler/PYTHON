class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self):

        #atributos de instancia
        self.nombre='Juan'
        self.apellido='Perez'
        self.edad=10
#objeto llamando a la clase persona y llamando el metodo init
persona=Persona()

print(persona.edad)