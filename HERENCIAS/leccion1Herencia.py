class Persona():
    def __init__(self,nNombre,nEdad):
        self.__nombre=nNombre
        self.__edad=nEdad
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nNombre):
        self.__nombre=nNombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,nEdad):
        self.__edad=nEdad
    def informacion_persona(self):

        return f'''
        nombre de la paersona: {self.nombre},
        edad de la persona: {self.edad} '''

    #definir los resultados de llamar directamente al objeto
    def __str__(self):
        return f'''
                nombre de la paersona: {self.nombre},
                edad de la persona: {self.edad} '''

class Empleado(Persona):
    def __init__(self,nSueldo,nNombre,nEdad):
        super().__init__(nNombre,nEdad)
        self.__sueldo=nSueldo

    @property
    def sueldo(self):
        return self.__sueldo
    @sueldo.setter
    def sueldo(self,nSueldo):
        self.__sueldo=nSueldo

    def informacion_empleado(self):
        return f'''
                nombre de la paersona: {self.nombre},
                edad de la persona: {self.edad}
                sueldo del empleado: {self.sueldo}
                '''

    def __str__(self):
        return f'''
                        {super().__str__()}
                        sueldo del empleado: {self.sueldo}
                        '''
if __name__ == '__main__':

    empleado1=Empleado(5000,'Daniel',35)
    print(empleado1.informacion_empleado())