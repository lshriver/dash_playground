import dash
from dash import html
import dash_bootstrap_components as dbc

# 1) Bootstrapping & server
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# 2) Tab definitions as data
TAB_CONFIG = [
    {
        "label": "Tab One",
        "label_class_name": "custom-tab-title",
        "active_label_class_name": "custom-tab-active",
        "content": "Content goes here…",
    },
    {
        "label": "Tab Two",
        "label_class_name": "custom-tab-title",
        "active_label_class_name": "custom-tab-active",
        "content": "More content…",
    },
    # —add more tabs here—
]

# 3) Build the Tabs component from TAB_CONFIG
tabs = dbc.Tabs(
    [
        dbc.Tab(
            label=tab["label"],
            label_class_name=tab["label_class_name"],
            children=html.P(tab["content"]),
        )
        for tab in TAB_CONFIG
    ]
)

# 4) Page layout
app.layout = html.Div(
    className="page-wrapper",
    children=[
        html.H1("Hello Gradient", className="gradient-text-1"),
        tabs,
        html.H2("Welcome Back", className="gradient-text-1")
    ],
)

if __name__ == "__main__":
    app.run(debug=True)