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
    for date, asteroids_list in data["near_earth_objects"].items():
        asteroids.extend(asteroids_list)
    
    return asteroids

def create_main_df(asteroids):
    df = pd.json_normalize(asteroids)
    df_main = df[[
        'neo_reference_id',
        'name',
        'absolute_magnitude_h',
        'is_potentially_hazardous_asteroid',
        'estimated_diameter.kilometers.estimated_diameter_min',
        'estimated_diameter.kilometers.estimated_diameter_max'
    ]].copy()
    df_main.rename(columns={
        'estimated_diameter.kilometers.estimated_diameter_min': 'diameter_min_km',
        'estimated_diameter.kilometers.estimated_diameter_max': 'diameter_max_km'
    }, inplace=True)
    df_main['diameter_min_km'] = df_main['diameter_min_km'].round(0).astype(int)
    df_main['diameter_max_km'] = df_main['diameter_max_km'].round(0).astype(int)

    return df_main

def create_close_approach_df(asteroids):
    rows = []
    for asteroid in asteroids:
        neo_id = asteroid.get("neo_reference_id")
        for event in asteroid.get("close_approach_data", []):
            row = {
                "neo_reference_id": neo_id,
                "close_approach_date": event.get("close_approach_date"),
                "relative_velocity_kph": event.get("relative_velocity", {}).get("kilometers_per_hour"),
                "miss_distance_km": event.get("miss_distance", {}).get("kilometers")
            }
            rows.append(row)
    df_close_approach = pd.DataFrame(rows)
    df_close_approach['relative_velocity_kph'] = df_close_approach['relative_velocity_kph'].round(2)
    df_close_approach['miss_distance_km'] = df_close_approach['miss_distance_km'].round(2)
    return df_close_approach