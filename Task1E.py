from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1E"""

    # Build list of stations
    stations = build_station_list()

    # Retrieve list of N rivers with most stations
    N = 7
    rivers_with_most_stations = rivers_by_station_number(stations, N)

    # Print result
    print([river_and_num_stations for river_and_num_stations in rivers_with_most_stations])



if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
