import pandas as pd

 # Cargar el conjunto de datos
df = pd.read_csv('datos_alquiler.csv')

# Eliminar registros duplicados
df = df.drop_duplicates()

# Guardar el conjunto de datos limpio
df.to_csv('datos_alquiler_limpios.csv', index=False)

# Rellenar valores faltantes con la mediana de la columna
df['precio_alquiler'] = df['precio_alquiler'].fillna(df['precio_alquiler'].median())

# Eliminar filas con valores faltantes
df = df.dropna()

# Guardar el conjunto de datos limpio
df.to_csv('datos_alquiler_limpios.csv', index=False)

# Convertir todas las columnas de texto a minúsculas
df['nombre_cliente'] = df['nombre_cliente'].str.lower()

# Convertir fechas al formato AAAA-MM-DD
df['fecha_alquiler'] = pd.to_datetime(df['fecha_alquiler']).dt.strftime('%Y-%m-%d')

# Guardar el conjunto de datos limpio
df.to_csv('datos_alquiler_limpios.csv', index=False)