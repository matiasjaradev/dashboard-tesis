# home.py
import plotly.graph_objects as go
from dash import Dash, html, dcc
from table import fig as table_fig  # tu tabla existente
from torta_plot import fig_pie_sector_dummy  # o importa desde el mismo archivo
from semantic_plot import fig_umap_dummy
from kpi_card import KpiCard
# ---- Theme para cards oscuras (alineado a assets/styles.css) ----
THEME = {
    "card":   "#111827",                 # mismo que --card
    "text":   "#ffffff",
    "muted":  "#a0a6b2",
    "grid":   "rgba(255,255,255,.06)",   # grilla suave
    "axis":   "rgba(255,255,255,.35)",   # eje/labels
    "accent": "#7C83FF",                 # color barras emociones
    # paleta sentimientos (ajústala a tu gusto)
    "pos":    "#10B981",                 # verde
    "neg":    "#EF4444",                 # rojo
    "neu":    "#9CA3AF"                  # gris
}

def apply_dark_card(fig):
    """Aplica colores del tema a una figura Plotly para que se vea como la card."""
    fig.update_layout(
        paper_bgcolor=THEME["card"],
        plot_bgcolor=THEME["card"],
        font=dict(color=THEME["text"]),
        margin=dict(l=40, r=20, t=60, b=40)
    )
    fig.update_xaxes(
        showgrid=True, gridcolor=THEME["grid"],
        zeroline=False, linecolor=THEME["axis"],
        tickfont=dict(color=THEME["text"]),
        title_font=dict(color=THEME["text"])
    )
    fig.update_yaxes(
        showgrid=True, gridcolor=THEME["grid"],
        zeroline=False, linecolor=THEME["axis"],
        tickfont=dict(color=THEME["text"]),
        title_font=dict(color=THEME["text"])
    )
    return fig

# -------- Data dummy ----------
EMOTIONS_LABELS = ["ANGER", "DISGUST", "FEAR", "JOY", "OTHERS", "SADNESS", "SURPRISE"]
EMOTIONS_VALUES = [0.05, 0.02, 0.01, 0.01, 0.81, 0.01, 0.09]

SENT_LABELS = ["NEU", "POS", "NEG"]
SENT_VALUES = [0.71, 0.02, 0.27]
SENT_COLORS = ["green", "red", "gray"]

# -------- Fig builders ----------
def fig_emociones(labels, values, comentario_n=49):
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            marker_color=THEME["accent"],             # barras acorde a tu tema
            text=[f"{v:.2f}" for v in values],
            textposition="outside",
        )
    )
    fig.update_yaxes(range=[0, 1], title="Probabilidad")
    fig.update_xaxes(tickangle=-25)
    fig.update_layout(
        title=f"<b>Comentario - Emociones</b>",
        uniformtext_minsize=10, uniformtext_mode="hide",
    )
    return apply_dark_card(fig)                      # <<— aplica el tema

pie_fig = fig_pie_sector_dummy()
pie_fig = apply_dark_card(pie_fig)  # usa tu helper para matchear la card

umap_fig = fig_umap_dummy()
umap_fig = apply_dark_card(umap_fig)  # usa tu helper para el tema oscuro


def fig_sentimientos(labels, values, colors=None, comentario_n=49):
    # Si no pasas colores, usamos los del tema:
    palette = colors or [THEME["neu"], THEME["pos"], THEME["neg"]]
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=labels,
            y=values,
            marker_color=palette,
            text=[f"{v:.2f}" for v in values],
            textposition="outside",
        )
    )
    fig.update_yaxes(range=[0, 1], title="Probabilidad")
    fig.update_layout(
        title=f"<b>Comentario - Sentimientos</b>",
        uniformtext_minsize=10, uniformtext_mode="hide",
    )
    return apply_dark_card(fig)  
# -------- App ----------
app = Dash(__name__)

# app.layout = html.Div(
#     className="page",
#     children=[
#         html.H2("Dashboard de Comentarios", className="page__title", style={"margin-left": "20px"}),

#         # grid responsive
#         html.Div(
#             className="grid",
#             style={"margin": 30},
#             children=[
#                 html.Div(className="card", children=[
#                     dcc.Graph(figure=table_fig, config={"displayModeBar": False})
#                 ], style={"width": 860, "height": 500}),
#                 html.Div(className="card", children=[
#                     dcc.Graph(figure=fig_emociones(EMOTIONS_LABELS, EMOTIONS_VALUES),
#                               config={"displayModeBar": False})
#                 ], style={"width": 500, "height": 500}),
#                 html.Div(className="card", children=[
#                     dcc.Graph(figure=fig_sentimientos(SENT_LABELS, SENT_VALUES, SENT_COLORS),
#                               config={"displayModeBar": False})
#                 ], style={"width": 500, "height": 500}),
#                html.Div(className="card", children=[
#                dcc.Graph(figure=pie_fig, config={"displayModeBar": False})
#                 ], style={"width": 500, "height": 500}),
#                 # En tu layout, agrega otra card:
#                 html.Div(className="card", children=[
#                 dcc.Graph(figure=umap_fig, config={"displayModeBar": False})]),
#             ],
#         ),
#     ],
# )


app = Dash(__name__)
app.layout = html.Div(className="page", children=[
    html.H2("Dashboard de Comentarios", className="page__title"),
    html.Div(className="grid", children=[

        html.Div(className="card card--table", children=[
            dcc.Graph(figure=table_fig, config={"displayModeBar": False})
        ]),

        html.Div(className="card card--emo", children=[
            dcc.Graph(figure=fig_emociones(EMOTIONS_LABELS, EMOTIONS_VALUES),
                      config={"displayModeBar": False})
        ]),

        html.Div(className="card card--sent", children=[
            dcc.Graph(figure=fig_sentimientos(SENT_LABELS, SENT_VALUES, SENT_COLORS),
                      config={"displayModeBar": False})
        ]),

        html.Div(className="card card--pie", children=[
            dcc.Graph(figure=pie_fig, config={"displayModeBar": False})
        ]),

        # KPI: trae class "kpi-card" -> caerá en el área 'kpi'
        KpiCard(current="DERECHA", previous="Decidido", yoy="común kasier es la mejor opcion", candidato="Kaiser", title=None, id="kpi-ventas"),

        html.Div(className="card card--umap", children=[
            dcc.Graph(figure=umap_fig, config={"displayModeBar": False})
        ]),
    ]),
])

if __name__ == "__main__":
    app.run(debug=True, port=10000)

