#contexto estatico es cuando se esta definiendo la clase

#contexto dinamico es cuando ya se pueden crear objetos de la clase



class MiClase():


    variable_clase='Valor variable clase'
    def __init__(self,nVariable_instancia):

        self.variable_instancia=nVariable_instancia

    # Un decorador permite modificar el metodo que va a afectar
    # @static el decorador static va a hacer que el metodo se asocie con la clase en si misma y no con los objetos
    # un metodo estatico no puede acceder a las variables de instancia
    # un metodo estatico no recibe la palabra self
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # un metodo de clase si recibe un contexto de clase
    # se puede acceder a las variables de clase
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)



print(MiClase.variable_clase)
MiClase.metodo_estatico()

MiClase.metodo_clase()


mi_objeto1=MiClase('Variable de instancia')
#un contexto dinamico si puede acceder a un contexto estatico pero los contextos estaticos no pueden acceder
# a los contextos dinamicos

# los metodos propios de la clase no pueden acceder a los objetos pero los objetos si pueden acceder a los
# metodos de la clase
mi_objeto1.metodo_clase()