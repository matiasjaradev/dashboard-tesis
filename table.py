import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

df = pd.read_csv("df_final.csv")

# Limpia la fecha (más simple que regex). Si quieres quitar la hora "00:00:00":
# df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime("%Y-%m-%d")
# Si quieres dejar fecha y hora:
df["fecha"] = pd.to_datetime(df["fecha"]).dt.strftime("%Y-%m-%d %H:%M:%S")

# Colores (modo oscuro)
BG_TRANSPARENT = "rgba(0,0,0,0)"
TXT = "#ffffff"
HEADER_BG = "rgba(255,255,255,.06)"
GRID_ROW = "rgba(255,255,255,.03)"
LINE = "rgba(255,255,255,.10)"

# Zebra por fila (mismo largo que el DataFrame)
row_colors = np.where(np.arange(len(df)) % 2 == 0, BG_TRANSPARENT, GRID_ROW).tolist()

fig = make_subplots(rows=1, cols=1, specs=[[{"type": "table"}]])

fig.add_trace(
    go.Table(
        header=dict(
            values=["Fecha", "Autor", "Likes", "Dislikes"],
            align="center",
            font=dict(size=13, color=TXT, family="Inter, Segoe UI, sans-serif"),
            fill_color=HEADER_BG,
            line_color=LINE,
            height=28,
        ),
        cells=dict(
            values=[df["fecha"], df["autor"], df["likes"], df["dislikes"]],
            align="left",
            font=dict(size=12, color=TXT, family="Inter, Segoe UI, sans-serif"),
            fill_color=[row_colors, row_colors, row_colors, row_colors],  # zebra
            line_color=BG_TRANSPARENT,   # sin bordes “duros”
            height=26,
        ),
        columnwidth=[140, 200, 80, 80],  # ajusta anchos a gusto
    ),
    row=1, col=1
)

fig.update_layout(
     title={
        "text": "<b>Autores Comentarios</b>",
        "x": 0.02,
        "xanchor": "left",
        "font": {"color": "white", "size": 18}
          # <-- color y tamaño
    },
    title_x=0.02,
    paper_bgcolor=BG_TRANSPARENT,   # fondo transparente (útil dentro de tu card)
    plot_bgcolor=BG_TRANSPARENT,
    height=500,                     # controla alto
    width=840,                      # controla ancho
    margin=dict(l=16, r=16, t=48, b=16),
)

fig.show()
