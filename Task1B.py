from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Display data from 3 stations:
    sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))

    # Print the name, town and distance of the 10 closest stations from Cambridge city centre
    print([(station[0].name, station[0].town, station[1]) for station in sorted_stations[:10]])

    # Print the name, town and distance of the 10 furthest stations from Cambridge city centre
    print([(station[0].name, station[0].town, station[1]) for station in sorted_stations[-10:]])


if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()
