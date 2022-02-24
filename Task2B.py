from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2B"""

    # Build list of stations and get water
    stations = build_station_list()
    update_water_levels(stations)

    # Get a list of all stations with relative water level above 0.8
    over_threshold = stations_level_over_threshold(stations, 0.8)

    # Print the name of the stations and their corresponding relative water levels
    for station in over_threshold:
        print(f"{station[0].name} {station[1]}")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
