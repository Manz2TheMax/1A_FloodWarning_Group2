from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    # Filter list of stations by distance to those within 10km of the Cambridge city centre, sorted by name alphabetically
    filter_radius = 10
    cam_centre = (52.2053, 0.1218)
    station_names_within_radius = stations_within_radius(stations, cam_centre, filter_radius)
    station_names_within_radius.sort()

    # Print list of names
    print(station_names_within_radius)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
