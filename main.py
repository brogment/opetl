# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
# if __name__ == '__main__':
#     print_hi('PyCharm')


import os
from dotenv import load_dotenv
import requests
import pandas as pd
# import json
import sqlite3
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)

load_dotenv()

API_KEY = os.getenv("API_KEY")
start_date = "2025-01-01"
end_date = "2025-01-07"

url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"
response = requests.get(url)
data = response.json()

# print(json.dumps(data, indent=2))

# with open("neo_data.json","w") as f:
#     json.dump(data, f, indent=2)

asteroids = data["near_earth_objects"][start_date]
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

close_approach_rows = []
for index, asteroid in df.iterrows():
    neo_id = asteroid['neo_reference_id']
    for event in asteroid.get("close_approach_data", []):
        row = {
            "neo_reference_id": neo_id,
            "close_approach_date": event.get("close_approach_date"),
            "relative_velocity_kpm": event.get("relative_velocity", {}).get("kilometers_per_hour"),
            "miss_distance_km": event.get("miss_distance", {}).get("kilometers")
        }
        close_approach_rows.append(row)
df_close_approach = pd.DataFrame(close_approach_rows)

df_close_approach['relative_velocity_kpm'] = df_close_approach['relative_velocity_kpm'].round(2)
df_close_approach['miss_distance_km'] = df_close_approach['miss_distance_km'].round(2)


# database connection
conn = sqlite3.connect("nasa_neo.db")
df_main.to_sql("asteroids", conn, if_exists="replace", index=False)
df_close_approach.to_sql("close_approach", conn, if_exists="replace", index=False)

df_asteroids = pd.read_sql_query("SELECT * FROM asteroids", conn)

conn.close()

# plotting histogram

plt.hist(df_asteroids["absolute_magnitude_h"].dropna(), bins=20, edgecolor="black")
plt.title("Distribution of Absolute Magnitude")
plt.xlabel("Absolute Magnitude (H)")
plt.ylabel("Frequency")
plt.show()