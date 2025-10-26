import plotly.graph_objects as go
from dash import Dash, html, dcc
from table import fig as figure

app = Dash(__name__)
fig = figure

app.layout = html.Div(
    className="page",
    children=[
        html.Div(
            children=[
                dcc.Graph(figure=fig, className="card")
            ],
            style= {"width": 860 }
        )
    ]
)


if __name__ == "__main__":
    app.run(debug=True, port=10000)

