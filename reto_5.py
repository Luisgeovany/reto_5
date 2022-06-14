import json

import pandas as pd

df = pd.read_csv("AMAZON.csv")

# Crear columna de resta Close - Open
df['Diferencia Close-Open'] = round(df['Close'] - df['Open'], 4)

# Crear columna Diferencia_absoluta_close-high
df['Diferencia_absoluta_close-high'] = abs(df['Diferencia Close-Open'])

# Crear columna Comportamiento_la_accion
df['Comportamiento_de_la_accion'] = ''

# condicionales
df.loc[df['Diferencia Close-Open'] > 0, 'Comportamiento_de_la_accion'] = 'SUBE'
df.loc[df['Diferencia Close-Open'] < 0, 'Comportamiento_de_la_accion'] = 'BAJA'
df.loc[df['Diferencia Close-Open'] == 0, 'Comportamiento_de_la_accion'] = 'ESTABLE'

# Crear un nuevo dataframe a partir del que ya tenemos
df2 = df[['Date', 'Comportamiento_de_la_accion', 'Diferencia_absoluta_close-high']]

# Cambiar nombre a la columna Date en el df2
df3 = df2.rename({'Date': 'Fecha '}, axis=1)

# Crear archivo analisis_archivo.csv
df3.to_csv('analisis_archivo.csv', index=False, sep=' ')

# Obtener fecha y valor minimo de la columna Volume
i_min_volume = df['Volume'].idxmin()  # obtenemos el indice de la fecha
fecha_min_volume = df.at[i_min_volume, 'Date']
min_volume = df['Volume'].min()

# Obtener la media
media_volume = df['Volume'].mean()

# obtener fecha mayor diferencia y mayor fiferencia
i_max_diferencia = df['Diferencia_absoluta_close-high'].idxmax()  # obtenemos el indice de la fecha
fecha_max_diferencia = df.at[i_max_diferencia, 'Date']
max_diferencia = df['Diferencia_absoluta_close-high'].max()

# obtener fecha menor diferencia y menor diferencia
i_min_diferencia = df['Diferencia_absoluta_close-high'].idxmin()  # obtenemos el indice de la fecha
fecha_min_diferencia = df.at[i_min_diferencia, 'Date']
min_diferencia = df['Diferencia_absoluta_close-high'].min()

detalles_dict = {
    'date_lowest_volume' : fecha_min_volume,
    'lowest_volume' : str(min_volume),
    'mean_volume' : str(media_volume),
    'date_greatest_difference' : fecha_max_diferencia,
    'greatest_difference' : str(max_diferencia),
    'date_smallest_difference' : fecha_min_diferencia,
    'smallest_difference': str(min_diferencia)
}

with open('detalles.json','w') as archivo:
    json.dump(detalles_dict,archivo)



