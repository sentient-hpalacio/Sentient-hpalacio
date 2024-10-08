import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('metric_mapping_OWF.csv')

# Crear una lista vacía para almacenar las nuevas filas
new_rows = []

# Iterar sobre cada fila del DataFrame original
for index, row in df.iterrows():
    # Añadir la fila original
    new_rows.append(row)

    # Crear 5 nuevas filas para cada fila original
    for i in range(1, 6):
        if row['component'] in ['GBX', 'GEN', 'NAC', 'MS-BRG-RS', 'MS-BRG-GS']:
            # Modificar solo la columna 'Edad' (puedes cambiar la lógica de modificación)
            new_row = row.copy()  # Hacemos una copia de la fila original
            new_row['pc'] = f'PC{i}'  # Modifica la columna 'Edad'
            new_row['varnames'] = new_row['varnames'] + f'-PC{i}'
            # Añadir la nueva fila a la lista
            new_rows.append(new_row)

# Convertir la lista de nuevas filas en un DataFrame
df_expanded = pd.DataFrame(new_rows)

df_expanded.to_csv('metric_mapping_OWF_out.csv', index=False)
print("\nDataFrame modificado con nuevas filas:")
print(df_expanded)
