class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self,nNombre,nApellido,nEdad):

        #atributos de instancia
        self._nombre=nNombre
        self.__apellido=nApellido
        self._edad=nEdad

    def mostrar_detalles(self):
        print(f'''la persona tine los siguientes atributos
                    nombre {self._nombre}
                    apellido {self.__apellido}
                    edad {self._edad}
                    ''')
#no se deberia acceder a atributos con guion bajo por fuera de nuestra clase
# ossea persona._nombre no se deberia hacer. el guion bajo es una sugerencia al programador aunque si se cambia
# si uno quiere ser restrictivo pone doble guion bajo a los atributos
persona=Persona('Juan','Perez',10,)
# la restriccion de un guion bajo existe para _nombre pero si se permite modificar por fuera de la clase
persona._nombre='Daniel'
# si bien el atributo existe como esta con doble guion bajo no deja que se manipule por fuera de la clase
persona.__apellido='juan'
print(persona.mostrar_detalles())



print(persona.mostrar_detalles())