from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H1("NASA NeoWs Dashboard"),
        html.Div([
            dcc.Input(
                id='start-date',
                type='text',
                placeholder='Start Date (YYYY-MM-DD)',
                value='2015-01-01'
            ),
            dcc.Input(
                id='end-date',
                type='text',
                placeholder='End Date (YYYY-MM-DD)',
                value='2015-01-07'
            ),
            html.Button('Submit', id='submit-button')
        ]),
        dcc.Graph(id='asteroid-chart'),
        html.Div(id='output-data')
    ])
