import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash( __name__,
    assets_folder='/workspaces/dash_playground/assets/'
    )
server = app.server  # expose for WSGI servers

app.layout = html.Div(
    className='page-wrapper',
    children=[
        html.H1("gradient-text-1",
            className='gradient-text-1'),
        html.H2("gradient-text-2",
            className='gradient-text-2'),
        html.H2("gradient-text-3",
            className='gradient-text-3'),
        html.H2("gradient-text-4",
            className='gradient-text-4'),

        html.H2('gradient-text-1',
                className='gradient-text-2'),
        html.P('Key Facts:',
                className='gradient-text1',
                style={'fontSize': '40px'}),
        html.Ul([
            html.Li('Number of Economies: 170'),
            html.Li('Temporal Coverage: 1974 - 2019'),
            html.Li('Update Frequency: Quarterly'),
            html.Li('Last Updated: March 18, 2020'),
            html.Li([
                'Source: ',
                    html.A(children='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database',
                            href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
            ])
        ])
    ]
)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8050)