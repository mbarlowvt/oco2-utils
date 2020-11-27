import requests
from typing import List

from models.flux_tower import FluxTower


# Loose mapping of https://co2.jpl.nasa.gov/developer/grid_api
def beginning_date(tower: FluxTower):
    return r'tMin=' + str(tower.data_start) + r'-01-01T00:00:00Z'


def end_date(tower: FluxTower):
    return r'tMax=' + str(tower.data_end) + r'-12-31T23:59:59Z'


def latitude_min(tower: FluxTower, precision=.0001):
    return r'latMin=' + str(tower.latitude - precision)


def latitude_max(tower: FluxTower, precision=.0001):
    return r'latMax=' + str(tower.latitude + precision)


def longitude_min(tower: FluxTower, precision=.0001):
    return r'lonMin=' + str(tower.longitude - precision)


def longitude_max(tower: FluxTower, precision=.0001):
    return r'lonMax=' + str(tower.longitude + precision)


def variables(vs: List[str]):
    v = r''
    for var in vs:
        v = v + 'variable=' + var + r';'
    return v

def formatEmail(email: str):
    formattedEmail = r''
    if email != '':
        formattedEmail = r'email=' + email
    return formattedEmail


class GridApi:
    url = 'http://co2.jpl.nasa.gov/wps/'

    def __init__(self, email='', dataset='OCO2L2Stdv10', precision=.0001):
        self.dataset = dataset
        self.precision = precision
        self.email = email

    # Going the route of string formed query params. Requests seems to be fighting me on the param parsing a bit
    def generate_grid_query_params(self, tower: FluxTower, vs: List[str]):
        return r'?service=wps&version=1.0.0&request=execute&identifier=grid&datainputs=dataset=' + self.dataset + r';' + \
           beginning_date(tower) + r';' + end_date(tower) + r';' + longitude_min(tower, self.precision) + r';' \
               + longitude_max(tower, self.precision) + r';' + \
           latitude_min(tower, self.precision) + r';' + latitude_max(tower, self.precision) + r';' + \
           variables(vs) + \
           r'format=netcdf;' + formatEmail(self.email) + r'&status=true&storeExecuteResponse=true'

    def get_tower_query(self, tower, vs: List[str]):
        query_params = self.generate_grid_query_params(tower, vs)
        print(query_params)
        return requests.get(self.url + query_params)
