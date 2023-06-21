planetas={'mar','tierr','ven'}

#un ser no tiene orden ni indices
# un ser no acepta duplicados

#imprima si existe el elemnto mar en el set planetas
print('mar' in planetas)

#para agregar elemetos al set

planetas.add('cas')
print(planetas)
#remove elimina elemento del set especificando el elemento si no existe da error
planetas.remove('cas')
print(planetas)
planetas.remove('alala')

#discard elimina elemento pero si no existe el elemento no sale error como el metodo remove

planetas.discard('cas')

#limpiar set
planetas.clear()

#eliminar set de la memoria
del planetas