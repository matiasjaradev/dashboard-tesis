# torta_plot.py (o en home.py)
import plotly.graph_objects as go

SECTOR_COLORS = {
    "Derecha":  "#1f77b4",
    "Izquierda":"#EF4444",
    "Centro":   "#9CA3AF",
}

def fig_pie_sector_dummy(
    labels=("Derecha","Izquierda","Centro"),
    values=(67.3, 28.8, 3.8),
    title="Intención por sector"
):
    fig = go.Figure(
        go.Pie(
            labels=labels,
            values=values,
            hole=0.45,                 # donut
            sort=False,                # mantiene el orden que pasas
            direction="clockwise",
            marker=dict(colors=[SECTOR_COLORS[l] for l in labels]),
            textinfo="label+percent",  # etiqueta y %
            hovertemplate="%{label}: %{value:.1f}%<extra></extra>"
        )
    )
    fig.update_layout(
        title=f"<b>{title}</b>",
        showlegend=False,
        margin=dict(l=40, r=20, t=50, b=40),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ffffff"),
        height=340
    )
    return fig
