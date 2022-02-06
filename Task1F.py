from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list()

    #Find stations with inconsistent typical range data
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Extract list of names and sort alphabetically
    station_names_list = [station.name for station in inconsistent_stations]
    station_names_list.sort()

    # Print list of names
    print(station_names_list)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
