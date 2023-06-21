from Orden import Orden
from Producto import Producto

producto1 = Producto('camisa', 100.00)
print(producto1)

producto2 = Producto('pantalon', 150.00)
print(producto2)

producto3 = Producto('calsetines', 10.00)
print(producto3)

producto4 = Producto('bluza', 70.00)
print(producto4)


lista_productos1 = [producto1, producto2]
lista_productos2 = [producto3, producto4]
la_orden1 = Orden(lista_productos1)
print('se imprime la Orden 1'.center(50, '-'))
print(la_orden1)
print(f'total de la orden {la_orden1.id} es: {la_orden1.calcular_total()}')

print('agregar productos a la orden 1'.center(50,'-'))
la_orden1.agregar_productos(producto3)
print(f'total de la orden {la_orden1.id} es: {la_orden1.calcular_total()}')


la_orden2 = Orden(lista_productos2)
print('se imprime la orden 2'.center(50, '-'))
print(la_orden2)
print(f'total de la orden {la_orden2.id} es: {la_orden2.calcular_total()}')