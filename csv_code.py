import pandas as pd

# Cargar archivos originales
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Unir datasets
df = pd.concat([df1, df2, df3], ignore_index=True)

# Filtrar solo Pink Morsels
df = df[df["product"] == "pink morsel"]

# Crear columna sales
df["sales"] = df["quantity"] * df["price"]

# Mantener columnas necesarias
df = df[["date", "region", "sales"]]

# Convertir fecha
df["date"] = pd.to_datetime(df["date"])

# Guardar CSV limpio
df.to_csv("cleaned_data.csv", index=False)

print("CSV limpio creado: cleaned_data.csv")

