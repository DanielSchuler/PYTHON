#diccionario {llave:valor}

diccionario={
    #como llave cualquier tipo inmutable
    'IDE':'Integrated Development Environment',
    'OOP':'Object Oriented Programing',
    'DBMS': 'Database management System'
}

#largo
print(len(diccionario))

#un diccionario al igual que un set no tiene indices
#para acceder a los elementos debemos proporcioar la llave
print(diccionario['IDE'])
print(diccionario.get('IDE'))

#modificar elementos de diccionario
diccionario['IDE']='integrated development environment'

# recorrer elementos
for llave in diccionario:
    print(f'este es el valor de la llave {llave}:',diccionario.get(llave))


#para acceder al valor usando for en un diccionario se usa este metodo tambien

for llave,valor in diccionario.items():
    print(llave,valor)

# si solo se quiere recuperar las llaves
for llave in diccionario.keys():
    print(llave)

#para volver las llaves en una lista
print(list(diccionario.keys()))

#si solo se quiere obtener los valores

for valor in diccionario.values():
    print(valor)

#saber existencia de un elemento

print('IDE'in diccionario)
print('oop' in diccionario)

#agregar elemento al diccionario
diccionario['PK']='Primary Key'
print(diccionario)

# si agregamos una llave existente sobreescribimos su valor

#eliminar elemento especificando su llave

diccionario.pop('PK')