# OCO-2 Utils
Simple utilities for processing OCO-2 data from the [CO2 Virtual Science Data Environment](https://co2.jpl.nasa.gov/#mission=OCO-2). 

## API wrappers
The `api` directory includes thin wrappers for the following APIs:
- [query service](https://co2.jpl.nasa.gov/developer/query_service)
- [grid service](https://co2.jpl.nasa.gov/developer/grid_api)

They are a bit of a work in progress and require a bit of extra testing and tuning to ensure that they're passing valid payloads to the query backend service

## Post data retrieval processing
The script `transform_lite_dataset.py` is a high level geo-bounded outputs. It accepts `.nc` files listed in the `data` directory and filters their data points against the towers provided in the `cali_towers.csv` file within +/- .1 degrees lat/long. The resulting files are deposited in the `processed` directory.