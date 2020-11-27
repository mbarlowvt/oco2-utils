from models.flux_tower import extract_towers, FluxTower

# Get towers from file
from api.grid_api import GridApi

# Load towers from file
towers = extract_towers('cali_towers.csv')

# Extract for years that have data
filtered_towers = filter(FluxTower.useful_tower, towers)

# Set up grid api (optionally add precision here)
grid_api = GridApi(email=r'mike%40lowbar.dev', dataset='OCO2LtCO2v9', precision=1)

# Pick variables for the grid API
grid_vars = [
    "co2_column_strong_band_idpCO2",
    "co2_column_weak_band_idp",
    "aerosol_aod",
    "co2_grad_del",
    "co2_profile",
    "wind_speed",
    "retrieval_land_water_indicator",
    "retrieved_wet_air_column_layer_thickness",
    "retrieved_dry_air_column_layer_thickness",
    "albedo_o2a",
    "albedo_wco2",
    "albedo_sco2",
]

tower_responses = []
counter = 0
for tower in filtered_towers:
    print(counter)
    if counter >= 1:
        print("exiting")
        break
    else:
        print("exploring tower " + str(counter))
        resp = grid_api.get_tower_query(tower, grid_vars)
        tower_responses.append(resp.text)
        print(resp.text)
        print(resp.content)
        counter += 1

print(tower_responses)
