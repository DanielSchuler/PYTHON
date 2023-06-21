# archivos con with con esta sintaxis no toca usar un bloque try finally para cerrar el archivo

with open('prueba.txt','r',encoding='utf8') as archivo:
    print(archivo.read())

    #este metodo llama internamente a los metodos __enter__ y __exit__