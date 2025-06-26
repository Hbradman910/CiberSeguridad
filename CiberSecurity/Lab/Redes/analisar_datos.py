import pandas as pd
import numpy as np

n = 1000
np.random.seed(42)

ingresos = np.random.normal(loc=1000, scale=100, size=n)
costos = np.random.normal(loc=700, scale=80, size=n)
ganancia = ingresos - costos

df = pd.DataFrame({
    "Simulacion": np.arange(1, n + 1),
    "Ingresos": ingresos,
    "Costos": costos,
    "Ganancias": ganancia
})

excel_path = "Simulacion Montecarlo.xlsx"
df.to_excel(excel_path, index=False)

excel_path