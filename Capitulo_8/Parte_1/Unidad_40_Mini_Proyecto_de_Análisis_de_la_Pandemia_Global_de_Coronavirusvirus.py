#Unidad 40 – Mini Proyecto: Análisis de la Pandemia Global de Coronavirus

#Objetivo en clase
#Que los estudiantes entiendan cómo los datos abiertos (OurWorldInData) ayudan a tomar decisiones en salud pública y cómo se pueden analizar con Python.


#Durante la pandemia, gobiernos y científicos usaron datos abiertos para saber dónde estaban aumentando los contagios y cuántas personas se estaban vacunando. Hoy analizaremos un ejemplo con datos reales.

#Cargar dataset

import pandas as pd

df = pd.read_csv("covid.csv")
print(df.head())


#Ejemplo simplificado de columnas:

#Pais	Date	Vaccinations
#Spain	2021-05-01	35.2
#Panama	2021-05-01	20.1
#Mexico	2021-05-01	18.5


#Obtener el último dato de cada país

latest = df.groupby("Pais").last()


#Top 5 países con más vacunados

print(latest.sort_values("Vacunados", ascending=False).head(10))


#Mapa del mundo
#Con plotly.express un mapa interactivo:

import plotly.express as px

fig = px.choropleth(latest,
                    locationmode="Nombre pais",
                    color="Vacunados",
                    title="Vacunación COVID-19 por país")
fig.show()


#Discusión crítica
#Pregunta para los chicos: ¿Por qué algunos países tienen menos datos? ¿Qué problemas trae la falta de transparencia en una pandemia?