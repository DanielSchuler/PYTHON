class Persona:

    #inicializador __init__
    # __ dunder

    def __init__(self,nNombre,nApellido,nEdad):

        #atributos de instancia
        self.__nombre=nNombre
        self.__apellido=nApellido
        self.__edad=nEdad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nNombre):
        self.__nombre=nNombre
    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self,nApellido):
        self.__apellido=nApellido
    def mostrar_detalles(self):
        print(f'''la persona tine los siguientes atributos
                    nombre {self.__nombre}
                    apellido {self.__apellido}
                    edad {self.__edad}
                    ''')
    def __del__(self):
        print(f'Persona {self.__nombre} {self.__apellido}')

if __name__ == '__main__':

    # es recomendable usar atributos con doble guion bajo y usar el decorador property para que se llamen esos atributos
    # para usar el metodo como si fuera un atributo usamos el decorador @property
    persona=Persona('Juan','Perez',10,)
    # con el decorador property no necesito usar ()
    print(persona.nombre)
    persona.nombre='Philipp'
    print(persona.nombre)
    print(persona.apellido)
    persona.apellido='Falla'
    print(persona.apellido)
    persona.__nombre='jorge'
    print(persona.nombre)
    #persona._nombre='Daniel'
    # si bien el atributo existe como esta con doble guion bajo no deja que se manipule por fuera de la clase
    #persona.__apellido='juan'
    #print(persona.mostrar_detalles())



#print(persona.mostrar_detalles())