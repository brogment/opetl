from dash import html, dcc

def serve_layout():
    return html.Div([
        html.H1("NASA NeoWs Dashboard"),
        html.Div([
            dcc.DatePickerRange(
                id='date-picker-range',
                start_date_placeholder_text='Start Date (YYYY-MM-DD)',
                end_date_placeholder_text='End Date (YYYY-MM-DD)',
                display_format='YYYY-MM-DD',
                start_date='2025-01-01',
                end_date = '2025-01-07'
            ),
            html.Button('Submit', id='submit-button')
        ]),
        dcc.Graph(id='asteroid-chart'),
        html.Div(id='output-data')
    ])
