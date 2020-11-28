# OCO-2 Utils
Simple utilities for processing OCO-2 data from the [CO2 Virtual Science Data Environment](https://co2.jpl.nasa.gov/#mission=OCO-2). 

___
## Post data retrieval processing
The script `transform_lite_dataset.py` is a high level geo-bounded outputs. It accepts `.nc` files listed in the `data` directory and filters their data points against the towers provided in the `cali_towers.csv` file within +/- .1 degrees lat/long. The resulting files are deposited in the `processed` directory.

### TODOs
Most things in this section are due to a lack of netcdf manipulation knowledge
- Dataset is currently putting out what appears to be garbage data after filtering, need to make sure that it gets cleaned up
- Using `where` right now since the dataset does not seem to be loading in dimensions, so that should hopefully be improved to using `sel` eventually
- `open_mfdataset` does not seem happy with the custom files downloaded since it does not have dims in which it thinks combinations can occur

___
## Easiest way to get the data
I used the following [custom data product page](https://co2.jpl.nasa.gov/build/?dataset=OCO2L2Stdv10&product=FULL) to generate a custom dataset from the larger OCO-2 data pool. The results were able to take the 95.3GB lite dataset down to approximately 54MB for a subset of data variables we were interested in. Be prepared for it to take a while though, since the job I submitted took about 3 days to complete. It will notify you by email and give you 7 days to download once complete, so go ahead and pull it down locally at your earliest convenience.

___
## API wrappers
The `api` directory includes thin wrappers for the following APIs:
- [query service](https://co2.jpl.nasa.gov/developer/query_service)
- [grid service](https://co2.jpl.nasa.gov/developer/grid_api)

They are a bit of a work in progress and require a bit of extra testing and tuning to ensure that they're passing valid payloads to the query backend service.