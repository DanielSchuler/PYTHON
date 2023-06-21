


try:
    #abrimos el archivo
    # para que se pueda escribir caracteres especiales usamos utf8
    #tipo de open (r = read, a = append, w = write, x= create, w+ = write-read, r+ = read -write

    # para archivos en windows y con ruta especifica usar \\ para linux usar /
    archivo=open('prueba.txt','w',encoding='utf8')
    # escribimos en el archivo
    archivo.write('Agregamos información al archivo \n')

    archivo.write('Adios')

except Exception as e:
    print(e)
finally:
    archivo.close()