import logging as log

# modo DEBUG solo en desarrollo
# manejo de handler %(asctime)s maneja el tiempo que aparece en el log
# %(levelname)s agrega el tipo de nivel ... si es debug info warning error o critical
# %(filename)s indica el archivo que esta mandando el mensaje
# %(lineno)s numero de la linea donde se generor el error
# %(message)s mensaje que hemos agregado al log
# para mostrar la fecha de otra manera usamos datemft Hora(I) minutos(M) y segundos(S) y si es am o pm (p)
# en el handler indicamos que vamos a escribir un mensaje en el archivo capa_datos.log
# con el SreamHandler indicamos que vamos a mandar el mensaje a la consola

log.basicConfig(level=log.DEBUG,
                format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capa_datos.log'),
                    log.StreamHandler()
                ])


if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')