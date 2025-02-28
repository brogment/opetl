import requests
import pandas as pd
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_neo_data(start_date, end_date):
    url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    asteroids = []
    for date, asteroid_list in data["near_earth_objects"].items():
        asteroids.extend(asteroid_list)
    return asteroids

def create_main_df(asteroids):
    df = pd.json_normalize(asteroids)
    df_main = df[[
        'neo_reference_id',
        'name',
        'absolute_magnitude_h',
        'is_potentially_hazardous_asteroid',
        'estimated_diameter.meters.estimated_diameter_min',
        'estimated_diameter.meters.estimated_diameter_max'
    ]].copy()

    df_main.rename(columns={
        'estimated_diameter.meters.estimated_diameter_min': 'diameter_min_m',
        'estimated_diameter.meters.estimated_diameter_max': 'diameter_max_m'
    }, inplace=True)

    df_main['name'] = df_main['name'].str.extract(r'\(([^)]+)\)')
    df_main['diameter_min_m'] = df_main['diameter_min_m'].round(0).astype(int)
    df_main['diameter_max_m'] = df_main['diameter_max_m'].round(0).astype(int)

    return df_main

def create_close_approach_df(asteroids):
