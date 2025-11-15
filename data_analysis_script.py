# Importación de librerías requeridas por el programa ElevaTech
import pandas as pd
import numpy as np

# Datos de muestra: Simulación de resultados de gestión ambiental/administrativa
# La idea es tener datos que puedas relacionar con tu experiencia.
data = {
    'Proyecto': ['A', 'B', 'C', 'D', 'E'],
    'Inversion_USD': [15000, 22000, 8000, 35000, 12000],
    'Impacto_Ambiental': [0.15, 0.05, 0.30, 0.08, 0.25], # Ejemplo de un índice de impacto
    'Region': ['Norte', 'Sur', 'Norte', 'Centro', 'Sur'],
    'Status': ['Completo', 'Pendiente', 'Completo', 'Completo', 'Pendiente']
}

# 1. Crear un DataFrame (Usando Pandas)
df = pd.DataFrame(data)
print("--- DataFrame Inicial ---")
print(df.head()) # Muestra las primeras filas para inspección

# 2. Uso de una Función Básica (Requisito: escribir funciones básicas)
def clasificar_proyecto(impacto):
    """Clasifica el proyecto según el nivel de Impacto_Ambiental."""
    if impacto > 0.2:
        return 'Alto Riesgo'
    else:
        return 'Bajo Riesgo'

# Aplicar la función y crear una nueva columna
df['Clasificacion'] = df['Impacto_Ambiental'].apply(clasificar_proyecto)

print("\n--- DataFrame con Clasificación ---")
print(df[['Proyecto', 'Impacto_Ambiental', 'Clasificacion']])

# 3. Uso de Bucle y Estructuras (Requisito: listas, bucles)
proyectos_pendientes = []
# Iterar sobre las filas (usando iterrows o un bucle de lista/diccionario)
for index, row in df.iterrows():
    if row['Status'] == 'Pendiente':
        # Añadir a una lista (Estructura de datos)
        proyectos_pendientes.append(row['Proyecto'])

print(f"\nProyectos pendientes de seguimiento: {proyectos_pendientes}")

# 4. Cálculo Estadístico Rápido (Usando Numpy o Pandas)
inversion_total = np.sum(df['Inversion_USD'])
print(f"\nInversión total en proyectos (USD): {inversion_total}")

# 5. Filtrado con Cláusula WHERE (similar a SQL)
df_norte = df[df['Region'] == 'Norte']
print("\n--- Proyectos de la Región Norte ---")
print(df_norte)