alto = int(input('proportciona el alto del rectangulo: '))
ancho = int(input('proporciona el ancho del rectangulo: '))

resultado_area = alto*ancho
#resultado_perimetro= 2*alto + 2*ancho
resultado_perimetro= 2*(alto + ancho)
print(f'El area del rectángulo es {resultado_area}')
print(f'El perimetro del rectangulo es {resultado_perimetro}')