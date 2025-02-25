## Near-Earth Object (NEO) Dashboard and ETL Pipeline
This in an education project created for the purpose of furthoring my python and data science knowledge.
### Project Overview
This project extracts, transforms, and visualizes data from NASA's Near Earth Object Web Service (NeoWs). It provides insights into asteroid trends, potential hazards, and close approaches to Earth using Python, Pandas, and Dash.

##### Features
* ETL Pipeline: Fetches asteroid data from the NeoWs API and processes it into a structured format.
* Dashboard: Interactive visualization of asteroid approach distances, sizes, and hazard levels.
* CSV Export: Saves processed data locally for further analysis.

### Setup Instructions

#### Clone the Repository (bash)
```
git clone https://github.com/your-username/your-repo.git
cd your-repo
```
#### Create a Virtual Environment (bash)
```
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows (CMD/PowerShell)
```
#### Install Dependencies (bash)
```
pip install -r requirements.txt
```
#### Configure API Key
1. Create a .env file in the project root.
2. Add your NASA API key:
```
NASA_API_KEY=your_actual_api_key_here
```
#### How to Use
TODO

### Data Source & Attribution
This project uses data from NASA's Near Earth Object Web Service (NeoWs).

API Name: Asteroids - NeoWs
Provider: NASA
API Documentation: NeoWs API Docs
Citation:

NASA, "Near Earth Object Web Service (NeoWs)," available at https://api.nasa.gov/.

This project is open-source under the MIT License.