from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2C"""

    # Build list of stations and get water
    stations = build_station_list()
    update_water_levels(stations)

    # Retrieve 10 stations with highest relative water level
    N = 10
    highest_stations = stations_highest_rel_level(stations, N)

    #Print list of stations (with relative water level for each)
    for station in highest_stations:
        print(station.name, station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
