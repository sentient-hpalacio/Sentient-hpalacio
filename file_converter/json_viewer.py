import json
import os
import gzip
import csv


#config
input_path = './input'
results_path = './results'
filename = 'NEZ_T13_GBX2PS-ISOA.json.gz'


# Abrir y leer el archivo JSON comprimido (.gz)
with gzip.open(os.path.join(input_path, filename)) as file:
    data = json.load(file)

# Escribir los datos en un archivo CSV
csv_filename = os.path.join(results_path, f'{filename.split(".")[0]}.csv').replace("\\", "/")

with open(csv_filename, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Escribir los encabezados (keys del JSON)
    if isinstance(data, list):
        headers = data[0].keys()
        writer.writerow(headers)

        # Escribir las filas
        for item in data:
            for row in item['data']:
                writer.writerow([row])
    else:
        writer.writerow(data.keys())
        writer.writerow(data.values())
