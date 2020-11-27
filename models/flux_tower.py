from dataclasses import dataclass

from dataclass_csv import DataclassReader


@dataclass
class FluxTower:
    index: int
    latitude: float
    longitude: float
    years_of_data: str = ""
    site_start: int = 0
    site_end: int = 0
    data_start: int = 0
    data_end: int = 0

    def useful_tower(self) -> bool:
        return self.data_start != 0

    def no_missing_years(self) -> bool:
        return self.years_of_data.split(",").count == self.data_end - self.data_start


def extract_towers(tower_csv):
    towers = []
    with open(tower_csv) as tower_csv:
        csv_reader = DataclassReader(tower_csv, FluxTower)
        for tower in csv_reader:
            towers.append(tower)
    return towers
