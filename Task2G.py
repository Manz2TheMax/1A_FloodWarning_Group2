
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.geo import stations_by_town
from floodsystem.flood import get_town_flood_risk, get_flood_risk_rating

def run():
    """Requirements for Task 2G"""

    stations = build_station_list()
    update_water_levels(stations)
    towns = stations_by_town(stations)

    town_names = list(towns.keys())

    for i in range(10):
        print(f"{town_names[i]} {get_flood_risk_rating(get_town_flood_risk(town_names[i], towns))}")
        

if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()
