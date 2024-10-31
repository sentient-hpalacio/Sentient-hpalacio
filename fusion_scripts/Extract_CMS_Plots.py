import os
import shutil

#Config
string1= 'ISS-ISOA.'
string2= 'Test'
ruta_origen = r"C:\Users\hpala\OneDrive - Sentient Corporation\Liberty\CMS\OWF"
ruta_destino = r"C:\Users\hpala\OneDrive - Sentient Corporation\Liberty\CMS\OWF_lite"

def copiar_archivos_iso(origen, destino):
    # Recorre la estructura de directorios desde la carpeta origen
    for dir_ruta, subdirs, ficheros in os.walk(origen):
        # Reemplaza la ruta de origen por la de destino para mantener la estructura de carpetas
        ruta_relativa = os.path.relpath(dir_ruta, origen)
        ruta_destino = os.path.join(destino, ruta_relativa)

        # Crea la carpeta en el destino si no existe
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)

        # Copia solo los ficheros cuyo nombre contiene la cadena 'ISO'
        for fichero in ficheros:
            if string1 in fichero or string2 in fichero:
                ruta_fichero_origen = os.path.join(dir_ruta, fichero)
                ruta_fichero_destino = os.path.join(ruta_destino, fichero)
                shutil.copy2(ruta_fichero_origen, ruta_fichero_destino)
                print(f"Copiado: {ruta_fichero_origen} -> {ruta_fichero_destino}")


# Llamada a la función
copiar_archivos_iso(ruta_origen, ruta_destino)
