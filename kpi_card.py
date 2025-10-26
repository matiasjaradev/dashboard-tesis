# kpi.py
from dash import html
from typing import Optional

CARD_BG = "#111827"
TEXT    = "#FFFFFF"
PRIMARY = "#7C83FF"   # títulos o acentos
MINT    = "#6FE6E6"   # valores (como en tu imagen)

def KpiRow(label: str, value: str, value_color: str = MINT):
    return html.Div(
        className="kpi-row",
        children=[
            html.Div(label,  className="kpi-label"),
            html.Div(value,  className="kpi-value", style={"color": value_color}),
        ], style={"heigth": 500}
    )

def KpiCard(
    current="$600,192.55",
    previous="$459,438.01",
    yoy="30.64%",
    candidato= "Johanes Kaiser",
    title=None,
    id="kpi-ventas"      # <- cualquier string
):
    return html.Div(
        id=id, className="card kpi-card",
        style={"backgroundColor": CARD_BG, "color": TEXT},
        children=[
            html.Div(title, className="card__title") if title else None,
            KpiRow("Sector politico",  current),
            KpiRow("Intensión", previous, value_color="#88A8FF"),
            KpiRow("Comentario",   yoy),
            KpiRow("Candidato",   candidato),
        ]
    )
