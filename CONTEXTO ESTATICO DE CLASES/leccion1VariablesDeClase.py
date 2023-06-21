

class MiClase():

    # si se crea una variable por fuera del metodo init es una variable de clase y se asocia a la clase
    # y no a los objetos
    # Si un objeto modifica el valor, todos los otros objetos veran reflejado el cambio

    # esta variable de clase se asociara a cada uno de los objetos
    variable_clase='Valor variable clase'
    def __init__(self,nVariable_instancia):
        # esta variable se asocia a cada uno de los objetos
        # cada objeto tiene su valor y no se comparte entre los objetos
        self.variable_instancia=nVariable_instancia


# se puede acceder directamente a la variable de clase al momento de llamar a la clase
print(MiClase.variable_clase)

# para acceder a la variable de instancia se debe crear un objeto de la clase

mi_clase=MiClase('variable de instancia')
print(mi_clase.variable_instancia)

# desde el objeto tambien se puede acceder a la variable de clase
print(mi_clase.variable_clase)

#la clase puede crear variables de clases que los objetos pueden acceder

MiClase.variable_clase2='Variable de clase 2'

print('variable de clase 2 llamada por los objetos'.center(50,'-'))
#el id no la reconoce porque se creo al vuelo en el codigo
print(mi_clase.variable_clase2)