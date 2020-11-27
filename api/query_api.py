import requests

from models.flux_tower import FluxTower


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


# Loose mapping of https://co2.jpl.nasa.gov/developer/query_service
class QueryService:
    url = 'https://co2.jpl.nasa.gov/wps'

    def __init__(self, dataset='OCO2L2Stdv10', precision=.0001):
        self.dataset = dataset
        self.precision = precision

    # Going the route of string formed query params. Requests seems to be fighting me on the param parsing a bit
    def generate_query_params(self, tower: FluxTower) -> str:
        return r'?service=wps&version=1.0.0&request=execute&identifier=query&datainputs=dataset=' + self.dataset + r';' + \
           beginning_date(tower) + r';' + end_date(tower) + r';' + \
               longitude_min(tower, precision=self.precision) + r';' + longitude_max(tower, precision=self.precision) + \
               latitude_min(tower, precision=self.precision) + r';' + latitude_max(tower, precision=self.precision) + r';' + \
           r'resultType=list;serviceType=httpserver&rawdataoutput=output=@mimetype=application/json'

    def post_grid_query(self, tower: FluxTower):
        tower_qp = self.generate_query_params(tower)
        return requests.post(self.url + tower_qp)
