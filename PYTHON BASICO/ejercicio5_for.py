

# a diferencia del while el for itera sobre elementos o de datos

palabra='hola'
for letra in palabra:
    print(letra)


print('palabra reservada para terminar ciclos break')

for letra in palabra:
    reservada='o'
    if letra == reservada:
        print(f'encontre la letra reservada {reservada}')
        break
    print(letra)
else:
    print('se acabo el ciclo for')