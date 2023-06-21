
CORRECCION WINDOWS Y POSTGRESS NO MANDA EL ERROR QUE EL ERROR ES DEL USUARIO
# ruta de instalacion de postgres
# archivos de programas y postgresql seleccionamos carpeta que tenemos instalada y data

# C:\Program Files\PostgreSQL\13\data\postgresql.conf
# con notpad ++ editamos

# al final del archivo hacemos los cambios

lc_messages = 'en-US'
lc_monetary = 'en-US'
lc_numeric = 'en-US'
lc_time = 'en-US'