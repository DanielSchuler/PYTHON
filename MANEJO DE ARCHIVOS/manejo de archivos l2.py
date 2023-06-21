#leccion 1 abrir y leer linea por linea o linea especifica
try:
    archivo = open('prueba.txt','r',encoding='utf8')
    # se lee linea por linea imprimiendola
    #for linea in archivo:
    #    print(linea)



    # tambien se puede usar el metodo archivo.readlines que devuelve un arreglo con la info del archivo
    # print(archivo.readlines())

    #si quiero acceder a una linea en especifico
    print(archivo.readlines()[0])
except Exception as e:
    print(f'Se totio el archvo {e}')

finally:
    print('termino la ejecucion del archivo')
    archivo.close()


#leccion 2 anexar informacion de un archivo a otro
try:
    # abrimos el archivo 1
    archivo1 = open('prueba.txt', 'r', encoding='utf8')
    # abrimos el archivo 2 si no existe lo crea
    # como esta en modo a de apend cada vez que se corra agregara la info del archivo prueba a la copia
    # si queremos que reemplace la info se debe poner en modo w
    archivo2 = open('copia.txt','a',encoding='utf8')

    # escrbibimos la info del archivo pruebas al archivo copia

    archivo2.write(archivo1.read())

except Exception as e:
    print(f'Se totio el archvo {e}')

finally:
    print('termino la ejecucion del archivo')
    archivo1.close()
    archivo2.close()