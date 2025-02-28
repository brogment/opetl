from dash import Input, Output, State
import plotly.express as px
from extractTransform import fetch_neo_data, create_main_df


def register_callbacks(app):
    @app.callback(
        Output('asteroid-chart', 'figure'),
        Output('output-data', 'children'),
        Input('submit-button', 'n_clicks'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def update_dashboard(n_clicks, start_date, end_date):
        if not n_clicks:
            # Return empty chart and text on initial load
            return {}, "Enter a date range and press submit."

        # Fetch and process data using functions from etl.py
        asteroids = fetch_neo_data(start_date, end_date)
        df_main = create_main_df(asteroids)

        # Create a histogram of absolute magnitude using Plotly Express
        fig = px.histogram(df_main, x='absolute_magnitude_h',
                           nbins=20, title='Distribution of Absolute Magnitude')
        summary_text = f"Total asteroids: {len(df_main)}"
        return fig, summary_text
