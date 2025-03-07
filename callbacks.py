from dash import Input, Output, State
import plotly.express as px
from extractTransform import fetch_neo_data, create_main_df, create_close_approach_df


def register_callbacks(app):
    @app.callback(
        Output('asteroid-chart', 'figure'),
        Output('close-approach-chart', 'figure'),
        Output('output-data', 'children'),
        Input('submit-button', 'n_clicks'),
        State('date-picker-range', 'start_date'),
        State('date-picker-range', 'end_date')
    )
    def update_dashboard(n_clicks, start_date, end_date):
        if not n_clicks:
            return {}, {}, "Enter a date range and press submit."

        asteroids = fetch_neo_data(start_date, end_date)
        df_main = create_main_df(asteroids)
        df_close_approach = create_close_approach_df(asteroids)

        fig1 = px.histogram(df_main,
                            x='absolute_magnitude_h',
                            nbins=20,
                            title='Distribution of Absolute Magnitude',
                            labels={"absolute_magnitude_h": "Absolute Magnitude"})
        fig1.update_layout(yaxis_title="Asteroid Count")
        fig2 = px.scatter(df_close_approach,
                          x = 'miss_distance_km',
                          y = 'relative_velocity_kph',
                          title = 'Close Approach: Miss Distance vs. Relative Velocity',
                          labels={
                              "miss_distance_km": "Miss Distance (km)",
                              "relative_velocity_kph": "Relative Velocity (km/h)"
                          })
        fig2.update_xaxes(tickformat=",.2f")
        fig2.update_yaxes(tickformat=",.2f")
        summary_text = f"Total asteroids: {len(df_main)} | Total close approaches {len(df_close_approach)}"
        return fig1, fig2, summary_text
