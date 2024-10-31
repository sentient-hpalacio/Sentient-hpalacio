import shutil

import boto3
import os
import re

# User Inputs
bucket_name = 'central-results-storage-stg'
deployment_date = '2024-11'
pattern = r'^.*\.png$'

costumer = 'Liberty' #Upper case sensitive
local_dir = 'results_NBM_3_Liberty'

prefix = os.path.join(costumer, deployment_date).replace('\\', '/') + '/'
pattern = prefix + r'*NBM*/.*/.*\.png$'
string_to_match = 'NBM_'
# Crear patrón regex para coincidir con directorios que contienen la cadena especificada y archivos .png
pattern = rf'{prefix}{costumer}_{string_to_match}.*/.*3.png$'


# pattern =r'Liberty/2024-06/Liberty_NBM.*/.*2.png$'
#          'Liberty/2024-06/Liberty_NBM.*/.*2.png$'

def build_results_directories(files_to_download: list, local_dir: str) -> None:

    for t in files_to_download:
        tech_dir = os.path.join(local_dir, t.split('/')[2])
        if not os.path.exists(tech_dir):
            os.makedirs(tech_dir)
        else:
            shutil.rmtree(tech_dir)
            os.makedirs(tech_dir)



def descargar_archivos_s3(bucket_name, prefix, pattern, local_dir):
    """
    Descarga archivos de un bucket de S3 que cumplan con ciertos criterios en el nombre.

    :param bucket_name: Nombre del bucket de S3
    :param prefix: Prefijo común de los archivos a buscar
    :param pattern: Patrón regex para filtrar los nombres de los archivos
    :param local_dir: Directorio local donde se guardarán los archivos descargados
    """
    s3 = boto3.client('s3')

    continuation_token = None
    files_to_download = []

    # Listar todos los objetos en el bucket con el prefijo dado
    # response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)
    while True:
        # Listar objetos en el bucket con el prefijo dado
        if continuation_token:
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix, ContinuationToken=continuation_token)
        else:
            response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' not in response:
            break

        # Filtrar los objetos cuyos nombres coincidan con el patrón dado
        # r'Liberty/2024-06/Liberty_NBM.*/.*2.png$'
        files_to_download.extend([obj['Key'] for obj in response['Contents'] if re.search(pattern, obj['Key'])])

        if response.get('IsTruncated'):  # Continuar listando si hay más objetos
            continuation_token = response.get('NextContinuationToken')
        else:
            break

    if not files_to_download:
        print(f"No se encontraron archivos que coincidan con el patrón en el bucket '{bucket_name}'.")
        return

    # Descargar cada archivo filtrado
    build_results_directories(files_to_download, local_dir)
    for file_key in files_to_download:
        tech_dir = os.path.join(local_dir, file_key.split('/')[2]).replace('\\','/')
        local_file_path = f"{tech_dir}/{file_key.split('/')[-3]}_{file_key.split('/')[-2]}_{file_key.split('/')[-1]}"
        print(f"Descargando {file_key} a {local_file_path}...")
        s3.download_file(bucket_name, file_key, local_file_path)
        print(f"Descargado {file_key} a {local_file_path}.")


# Ejemplo de uso
# bucket_name = 'nombre-del-bucket'
# prefix = 'prefijo/de/los/archivos/'
# pattern = r'tu_patron_regex'  # Ejemplo: r'^.*\.txt$' para archivos .txt
# local_dir = 'directorio/local/de/descarga'

descargar_archivos_s3(bucket_name, prefix, pattern, local_dir)
