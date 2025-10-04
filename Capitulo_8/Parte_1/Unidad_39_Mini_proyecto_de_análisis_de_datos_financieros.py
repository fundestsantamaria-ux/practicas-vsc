#Unidad 39 – Mini Proyecto: Análisis de Datos Financieros

#Objetivo en clase
#Que los estudiantes apliquen lo aprendido en Python para analizar datos financieros básicos, identificar patrones y visualizar resultados, entendiendo su aplicación en el mundo real (ejemplo: empresas, bancos, inversionistas).

#Las empresas necesitan saber en qué gastan, cuánto ganan y cómo mejorar su rentabilidad. Hoy vamos a analizar datos financieros básicos para tomar decisiones.

#Cargar los datos ejemplo sencillo en CSV:

import pandas as pd

df = pd.read_csv("finanzas.csv")
print(df.head())


#Ejemplo de dataset:

#Mes	Ingresos	Gastos
#Ene	2000	    1500        
#Feb	2500	    1600      
#Mar	1800	    1700       



#Calcular utilidad

df["Utilidad"] = df["Ingresos"] - df["Gastos"]


#Identificar meses buenos y malos

print(df[df["Utilidad"] < 0])  # meses en pérdida


#Visualización

import matplotlib.pyplot as plt

df.plot(x="Mes", y="Utilidad", kind="bar")
plt.show()


#Discusión crítica
#Pregunta para los chicos: Si tu empresa pierde dinero en 2 meses seguidos, ¿qué decisión tomarías? ¿Reducir gastos o aumentar ingresos?