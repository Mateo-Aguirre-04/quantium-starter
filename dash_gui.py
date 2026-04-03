import datetime

import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load cleaned dataset (from previous task)
df = pd.read_csv("cleaned_data.csv")

# Ensure proper datetime format and sorting
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Aggregate sales by date
daily_sales = df.groupby("date")["sales"].sum().reset_index()

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

fig.add_annotation(
    x="2021-01-15",
    y=daily_sales["total_sales"].max(),
    text="Price Increase",
    showarrow=True,
    arrowhead=2,
    yshift=10
)

# Initialize app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualizer", style={"textAlign": "center"}),

    dcc.Graph(
        id="sales-line-chart",
        figure=fig
    )
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)