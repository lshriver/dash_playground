import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, 
                assets_folder='/workspaces/dash_playground/assets/',
                external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.layout = html.Div(
    [
      html.Div(
        className="feature-box",
        children=[
          html.Div(
            className="feature-box-content",
            children=[
              html.H4("My Project Title"),
              html.P("A short description of the project goes here."),
              dbc.Button("Learn More", color="primary")
            ]
          )
        ]
      ),

      html.Div(
        className="feature-box",
        children=[
          html.Div(
            className="feature-box-content",
            children=[
              html.H4("Another Resource"),
              html.P("Some details about this resource."),
              dbc.Button("View", color="secondary")
            ]
          )
        ]
      ),
    ],
    style={"padding": "40px"}  # optional page padding
)

if __name__ == "__main__":
    app.run(debug=True)