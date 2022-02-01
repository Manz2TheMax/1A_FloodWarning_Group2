from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Filter list of stations by distance to those within 10km of the Cambridge city centre
    filter_radius = 10
    cam_centre = (52.2053, 0.1218)
    station_list = stations_within_radius(stations, cam_centre, filter_radius)
    
    # Extract list of names and sort alphabetically
    station_names_list = [station.name for station in station_list]
    station_names_list.sort()

    # Print list of names
    print(station_names_list)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
