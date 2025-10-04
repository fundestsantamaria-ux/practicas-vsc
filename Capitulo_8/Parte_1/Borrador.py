import pandas as pd

# Datos de ejemplo
datos = {
    "Pais": ["Panama", "Mexico", "Argentina", "España"],
    "Casos": [50000, 120000, 80000, 150000],
    "Vacunados": [30000, 80000, 60000, 100000]
}

df = pd.DataFrame(datos)

# Guardar como CSV
df.to_csv("covid.csv", index=False)

print("Archivo covid.csv creado")
