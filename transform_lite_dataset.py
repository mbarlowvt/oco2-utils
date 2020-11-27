from models.flux_tower import extract_towers, FluxTower
import os

import xarray as xr

# Load towers from file
towers = extract_towers('resources/cali_towers.csv')

# Extract for years that have data
filtered_towers = filter(FluxTower.useful_tower, towers)

all_files = os.listdir('data')
print(all_files)


def filter_lat_long(lat_lims, long_lims, nc):
    # Returns the portion of nc between the given limits
    # lat_lims and long_lims are lists of the [minimum, maximum] values for latitude
    # and longitude desired from the netcdf file.
    # nc is the netcdf file.

    lats = nc.variables["lat"][:]
    longs = nc.variables["lon"][:]
    lat_inds = lats[
        (lats > lat_lims[0]) & (lats < lat_lims[1])
    ]
    long_inds = longs[
        (longs > long_lims[0]) & (longs < long_lims[1])
    ]
    return nc.sel(lat=lat_inds, lon=long_inds)


for file in all_files:
    print('processing file: ' + file)
    for tower in filtered_towers:
        all_data = xr.open_mfdataset('./data/' + all_files)
        print('processing tower ' + str(tower.index))
        savename = 'processed/' + str(tower.index) + '_' + file
        print(savename)
        # lat_lims = [tower.latitude - .1, tower.latitude + .1]
        # long_lims = [tower.longitude - .1, tower.longitude + .1]
        print(all_data.dims)
        # filtered_nc = filter_lat_long(lat_lims, long_lims, all_data)
        filtered_nc = all_data.sel(lat=(all_data['lat'] >= tower.latitude - .1) &
                                   (all_data['lat'] <= tower.latitude + .1), lon=(all_data['lon'] >= tower.longitude - .1) &
                                   (all_data['lon'] <= tower.longitude + .1)
                                   )
        filtered_nc.to_netcdf(path=savename, mode="w")
