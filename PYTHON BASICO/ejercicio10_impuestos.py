def calculadora(valor,impuestos):
    valorCI=(valor*impuestos/100)+valor
    return (f'''
            el valor sin impuestos es {valor}
            el valor del impuestos es del{impuestos}%
            el valor con impuestos seria del {valorCI}''')


valor=int(input('proporcione valor sin impuestos'))
impuestos= int(input(('proporvione el impuesto')))

print(calculadora(valor,impuestos))