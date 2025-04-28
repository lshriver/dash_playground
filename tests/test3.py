import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    className="page-wrapper",
    children=[
      html.H1("Hello Gradient", className="gradient-text-2"),
      dbc.Tabs(
        children=[
          dbc.Tab(
            label="Tab One",
            label_class_name="gradient-text-1",
            children=[html.P("Content goes here...")],
          ),
          dbc.Tab(
            label="Tab Two",
            label_class_name="gradient-text-3",
            children=[html.P("More content...")],
          ),
        ]
      )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)