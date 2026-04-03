import pandas as pd

# Load CSVs
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

df = pd.concat([df1, df2, df3], ignore_index=True)

print("Filas iniciales:", len(df))

# Normalizar producto
df["product"] = df["product"].astype(str).str.lower().str.strip()

# Filtrar
df = df[df["product"] == "pink morsel"]

print("Filas después del filtro:", len(df))

# 🔥 LIMPIAR PRICE (CLAVE)
df["price"] = df["price"].astype(str).str.replace("$", "", regex=False)

# Convertir a numérico
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

# Crear sales
df["sales"] = df["quantity"] * df["price"]

# Convertir fecha
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# 🔍 DEBUG antes de borrar
print("\nNulos:")
print(df[["date", "sales", "region"]].isna().sum())

# Limpiar datos
df = df.dropna(subset=["date", "sales", "region"])

print("Filas finales:", len(df))

# Guardar columnas finales
df = df[["date", "region", "sales"]]
df = df.sort_values("date")

df.to_csv("cleaned_data.csv", index=False)

print("\n✅ CSV limpio generado correctamente")
print(df.head())