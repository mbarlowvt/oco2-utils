from models.flux_tower import extract_towers, FluxTower
import os

import xarray as xr

# Load towers from file
towers = extract_towers('resources/cali_towers.csv')

# Extract for years that have data
filtered_towers = list(filter(FluxTower.useful_tower, towers))

all_files = os.listdir('data')
print(all_files)


for file in all_files:
    all_data = xr.load_dataset('data/' + file)
    print('Processing file ' + file)
    for tower in filtered_towers:
        print('processing tower ' + str(tower.index))
        savename = 'processed/' + str(tower.index) + '_' + file
        print(all_data.dims)
        filter_conditions = (all_data['lat'] >= tower.latitude - .1) & (all_data['lat'] <= tower.latitude + .1) & (
            all_data['lon'] >= tower.longitude - .1) & (all_data['lon'] <= tower.longitude + .1)
        filtered_nc = all_data.where(filter_conditions, drop=True)
        if(filtered_nc.dims['points_dimension'] > 0):
            print(filtered_nc.dims['points_dimension'])
            filtered_nc.to_netcdf(path=savename, mode="w")
