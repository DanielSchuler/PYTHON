from Orden import Orden
from Computadora import Computadora
from Monitor import Monitor
from Teclado import Teclado
from Raton import Raton
print('Datos de los Ratones'.center(50,'-'))

raton1=Raton('Cable','microsoft')
raton2=Raton('Bluetooth','klipxtreme')

print('Datos de los Teclados'.center(50,'-'))

teclado1=Teclado('Cable','microsoft')
teclado2=Teclado('Cable','hp')


print('Datos de los Monitores'.center(50,'-'))

monitor1=Monitor('Samsung',13)
monitor2=Monitor('LG',13)

print('Datos de las Computadoras'.center(50,'-'))
computadora1=Computadora('Microsoft123',monitor1,teclado1,raton1)
computadora2=Computadora('Ipack122',monitor2,teclado2,raton2)


lsitaComputadoras=[]
print('Datos de la orden'.center(50,'-'))
orden1=Orden(lsitaComputadoras)
print(orden1)
orden1.agreagar_computadora(computadora1)
orden1.agreagar_computadora(computadora2)
print(orden1)



