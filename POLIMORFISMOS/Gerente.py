from Empleado import Empleado
class Gerente(Empleado):

    def __init__(self,nNombre,nSueldo,nDepartamento):
        # tambien se puede usar super()__init__(nNombre,nSueldo)
        Empleado.__init__(self,nNombre,nSueldo)
        self.departamento=nDepartamento


    def __str__(self):
        #return  f'Gerente [Departamento: {self.departamento},{super().__str__()}]'
        return  f'Gerente [Departamento: {self.departamento},{Empleado.__str__(self)}]'


