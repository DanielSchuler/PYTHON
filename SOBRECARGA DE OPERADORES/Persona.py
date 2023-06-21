
class Sayayin:

    def __init__(self,nNombre,nEdad):
        self.__nombre=nNombre
        self.__edad=nEdad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def __str__(self):
        return f'sayayin [nombre:{self.nombre},edad:{self.edad}'


    #sobrecarga de operadores
    # sobrecarga del operador suma para unir los dos nombres de los sayayijes
    def __add__(self, other):


        return self.nombre[:(int(len(self.nombre)/2))] + other.nombre[int(len(other.nombre)/2):]


    # sobrecarga del operador resta para restar las edades de los dos sayayines

    def __sub__(self, other):

        return self.edad - other.edad
# en la sobrecarga de operadores llamariamos obj1 + obj2 que es equivalente a obj1.__add__(obj2)


sayayin2=Sayayin('Goku',40)
sayayin1=Sayayin('Vegeta',45)

sayayin_fusion_nombre= sayayin1+sayayin2
sayayin_fusion_edad=sayayin1-sayayin2
print(sayayin_fusion_nombre)
print(sayayin_fusion_edad)