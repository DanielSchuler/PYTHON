nombres=['dan','fil','nico','sandy']

print(nombres)
for nombre in nombres: # esto significa que para cada elemento en la lista de elementos haga
    print(nombre)
else:
    print('no hay mas nombres')

# append esto significa que añadimos a carla en la ultima posicion de la lista
nombres.append('karla')
print(nombres)
# insert esto significa que el elemento se inserta en el indice 2 y
# todos los otros elementos se mueven hacia la derecha
nombres.insert(2,'fabio')
print(nombres)

#remove esto significa que puedo eliminar un elemento por valor no por indice
nombres.remove('fabio')
print(nombres)
#pop esto significa que remueve el ultimo elemento de la lista
nombres.pop()
print(nombres)
#del y especificando indice esto significa que eliminamos elemento con el indice especificado
del nombres[0]
print(nombres)
#clear para limpiar la lista de todos los elementos
nombres.clear()
# del solito esto significa que elimina la lista de la memoria

del nombres