import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash( __name__,
    assets_folder='/workspaces/dash_playground/assets/',
    external_stylesheets=[dbc.themes.BOOTSTRAP]
    )
server = app.server  # expose for WSGI servers

app.layout = html.Div(
    className='page-wrapper', 
    children=[
        html.H1('gradient-text-2',
                className='gradient-text-2'),
        html.H2('gradient-text-3',
                className='gradient-text-3'),
        dbc.Tabs(className='gradient-text-1',
            children=[
            dbc.Tab(
                label='custom-tab-title',
                tab_class_name='custom-tab-active',
                active_tab_class_name='custom-tab-active',
                className='gradient-text-4',
                children=[ 
                    html.Ul([
                        html.Br(),
                        html.Li('Number of Economies: 170'),
                        html.Li('Temporal Coverage: 1974 - 2019'),
                        html.Li('Update Frequency: Quarterly'),
                        html.Li('Last Updated: March 18, 2020'),
                        html.Li([
                            'Source: ',
                            html.A('https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                                   href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
                        ])
                    ])
                ]
            ), 
            dbc.Tab(
                label='Project Info',
                children=[
                    html.Ul([
                        html.Br(),
                        html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
                        html.Li(['GitHub repo: ',
                            html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                                   href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')
                        ])
                    ])
                ]
            )
        ]),
    ]
)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8050)