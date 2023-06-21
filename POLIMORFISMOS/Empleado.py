class Empleado:

    def __init__(self, nNombre, nSueldo):
        self.nombre = nNombre
        self.sueldo = nSueldo

    def __str__(self):
        return f'Empleado:[Nombre:{self.nombre}, Sueldo:{self.sueldo}'

    # Polimorfismo Se puede acceder a este metodo desde el objeto hijo
    def mostrar_detalles(self):
        return self.__str__()