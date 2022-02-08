from floodsystem.geo import stations_by_river, rivers_with_station
from floodsystem.stationdata import build_station_list


def run_part_1(stations):
    """Requirements for Part 1 of Task 1D.
    For a list of MonitoringStation objects (stations), prints the names of 10 rivers."""

    # Print how many rivers have at least one monitoring station
    river_names = list(rivers_with_station(stations))
    river_names.sort()

    # Print the first 10 in alphabetical order
    print(f"{len(river_names)} stations. First 10 - {river_names[:10]}")


def run_part_2(stations):
    """Requirements for Part 2 of Task 1D.
    For a list of MonitoringStation objects (stations), prints the names of stations on rivers Aire, Cam and Thames."""

    # Dictionary containing river names and their corresponding stations
    rivers = stations_by_river(stations)

    # Print a list of stations on rivers Aire, Cam and Thames
    stations_on_aire = [station.name for station in rivers["River Aire"]]
    # Sort the list in alphabetical order
    stations_on_aire.sort()
    print(f"Stations on River Aire: {stations_on_aire}")

    stations_on_cam = [station.name for station in rivers["River Cam"]]
    stations_on_cam.sort()
    print(f"Stations on River Cam: {stations_on_cam}")

    stations_on_thames = [station.name for station in rivers["River Thames"]]
    stations_on_thames.sort()
    print(f"Stations on River Thames: {stations_on_thames}")


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")

    # Build list of stations
    stations_list = build_station_list()

    # Run parts 1 and 2
    run_part_1(stations_list)
    run_part_2(stations_list)
