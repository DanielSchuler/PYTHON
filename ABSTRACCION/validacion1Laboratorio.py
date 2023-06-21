from laboratorio1FiguraGeometrica import Cuadrado,Rectangulo,FiguraGeometrica

#no se puede instanciar una clase abstracta
#figura=FiguraGeometrica()


print('Creacion objeto Cuadrado'.center(50,'-'))
cuadrado1=Cuadrado(60,2,'Azul')
print(cuadrado1.area)
print(cuadrado1)
print('Validacion set'.center(50,'-'))
cuadrado1.alto=12
print(cuadrado1)
print('Creacion objeto Rectangulo'.center(50,'-'))

rectangulo1=Rectangulo(4,2,'rojo')
print(rectangulo1.area)
print(rectangulo1)

print('Metodo MRO=Methode Esolution Order'.center(50,'-'))
print(Cuadrado.mro())