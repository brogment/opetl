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
import json

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
    'estimated_diameter.kilometers.estimated_diameter_min',
    'estimated_diameter.kilometers.estimated_diameter_max'
]]

print(df_main.head())