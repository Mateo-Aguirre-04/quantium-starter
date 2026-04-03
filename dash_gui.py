import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load cleaned dataset (from previous ta2sk)
df = pd.read_csv("cleaned_data.csv")

# Ensure proper datetime format and sorting
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Aggregate sales by date
daily_sales = df.groupby("date")["sales"].sum().reset_index()
before = daily_sales[daily_sales["date"] < "2021-01-15"]["sales"].mean()
after = daily_sales[daily_sales["date"] >= "2021-01-15"]["sales"].mean()

print("Promedio antes:", before)
print("Promedio después:", after)

if after > before:
    print("Las ventas fueron MAYORES después del aumento")
else:
    print("Las ventas fueron MENORES después del aumento")

# Create line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

# Add vertical line for price increase date
fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red"
)
fig.update_layout(
    plot_bgcolor="#2c3e50",   # fondo del área del gráfico
    paper_bgcolor="#2c3e50",  # fondo externo
    font=dict(color="white")
)
fig.add_annotation(
    x="2021-01-15",
    y=daily_sales["sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=2,
    yshift=10
)

# Initialize app
app = Dash(__name__)

# Layout
result_text = (
    "Sales increased after the price change"
    if after > before
    else "Sales decreased after the price change"
)

app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", className="title"),

    html.H3(result_text, style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig,
        className="graph"
    )
    
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)