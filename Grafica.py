import pandas as pd
import matplotlib.pyplot as plt
ruta_archivo = 'energia.csv' #Cargar archivo
data = pd.read_csv(ruta_archivo)
ultimo_anio = data['Year'].max() #filtrar los ultimos 7 años
ultimos_7_anios = data[data['Year'] >= ultimo_anio - 6]
columnas_energia = ['Geo Biomass Other - TWh', 'Solar Generation - TWh',
                    'Wind Generation - TWh', 'Hydro Generation - TWh']
datos_energia = ultimos_7_anios[['Entity', 'Year'] + columnas_energia]
continentes = ['Africa', 'Asia', 'Europe', 'North America', 'South America', 'Oceania']
datos_continentes = datos_energia[datos_energia['Entity'].isin(continentes)]

for continente in continentes:
    datos_continente = datos_continentes[datos_continentes['Entity'] == continente]
    energia_por_anio = datos_continente.groupby('Year')[columnas_energia].sum()

    # Crear la gráfica apilada
    plt.figure(figsize=(10, 6))
    colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Colores para las energías
    # Crear las barras apiladas
    energia_por_anio.plot(
        kind='bar',
        stacked=True,
        color=colores,
        figsize=(10, 6),
        ax=plt.gca()  # Usa el eje actual
    )
    # Añadir título y etiquetas
    plt.title(f'Generación de Energía en {continente}', fontsize=14)
    plt.xlabel('Año', fontsize=12)
    plt.ylabel('TWh', fontsize=12)
    plt.legend(title='Tipo de Energía', bbox_to_anchor=(1.05, 1), loc='upper left')
    # Ajustar diseño
    plt.tight_layout()
    # Guardar la gráfica como PNG
    nombre_archivo = f"energia_{continente.lower().replace(' ', '_')}.png"
    plt.savefig(nombre_archivo, dpi=300)
    print(f"Gráfica guardada: {nombre_archivo}")

    # Cerrar la figura actual para evitar superposiciones
    plt.close()
