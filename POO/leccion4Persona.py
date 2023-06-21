class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self,nNombre,nApellido,nEdad,*args,**kwargs):

        #atributos de instancia
        self.nombre=nNombre
        self.apellido=nApellido
        self.edad=nEdad
        self.terminosTupla=args
        self.terminosDict=kwargs
    def mostrar_detalles(self):
        print(f'''la persona tine los siguientes atributos
                    nombre {self.nombre}
                    apellido {self.apellido}
                    terminosTupla {self.terminosTupla}
                    terminosDiccionario {self.terminosDict}
                    ''')
#enviar por parametro nombre,apellido y edad que son requeridos y ademas valores variables y atributos con llave valor
persona=Persona('Juan','Perez',10,'3163364424',28,29,39,fruta='manzana',verdura='zanahoria')
print(f'persona1 = {persona.nombre},{persona.apellido},{persona.edad}')


persona2=Persona('Karla','Gomez',15)
print(f'persona2 = {persona2.nombre},{persona2.apellido},{persona2.edad}')

print(persona.mostrar_detalles())