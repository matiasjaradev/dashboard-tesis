import plotly.graph_objects as go

# Coordenadas sintéticas (aprox. a tu imagen)
PTS = {
    "JeannetteJara":          (9.20, -9.85),
    "EvelynMatthei":          (8.72, -10.53),
    "MarcoEnriquezOminami":   (8.18, -9.82),
    "HaroldMayneNicholls":    (9.96, -10.41),
    "EduardoArtes":           (7.75, -11.02),
    "JohannesKaiser":         (9.03, -11.37),
    "FrancoParisi":           (9.98, -11.56),
    "JoseAntonioKast":        (8.18, -11.24),
}

# Colores por punto (elige los que quieras)
COLORS = {
    "JeannetteJara":        "#1f77b4",
    "EvelynMatthei":        "#d62728",
    "MarcoEnriquezOminami": "#9467bd",
    "HaroldMayneNicholls":  "#8c564b",
    "EduardoArtes":         "#2ca02c",
    "JohannesKaiser":       "#e377c2",
    "FrancoParisi":         "#ff7f0e",
    "JoseAntonioKast":      "#7f7f7f",
}

def fig_umap_dummy(title="Distancia semántica entre programas políticos (UMAP + fragmentos)"):
    xs = [PTS[k][0] for k in PTS]
    ys = [PTS[k][1] for k in PTS]
    names = list(PTS.keys())
    colors = [COLORS[k] for k in names]

    fig = go.Figure(
        go.Scatter(
            x=xs, y=ys,
            mode="markers+text",
            text=names,
            textposition="middle right",
            marker=dict(size=16, color=colors, line=dict(width=1, color="rgba(255,255,255,.8)")),
            hovertemplate="<b>%{text}</b><br>Dim 1: %{x:.2f}<br>Dim 2: %{y:.2f}<extra></extra>",
        )
    )
    fig.update_layout(
        title=f"<b>{title}</b>",
        xaxis_title="Dim 1",
        yaxis_title="Dim 2",
        margin=dict(l=50, r=30, t=60, b=50),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ffffff"),
        height=520,
    )
    fig.update_xaxes(showgrid=True, zeroline=False)
    fig.update_yaxes(showgrid=True, zeroline=False)
    return fig
