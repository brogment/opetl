import dash
from layout import serve_layout
from callbacks import register_callbacks

# Initialize the Dash app
app = dash.Dash(__name__)
app.layout = serve_layout()

# Register callbacks to link interactivity
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
