"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from haversine import haversine as hav  # haversine function for distance

def test_stations_within_radius():
    """Tests subroutine stations_within_radius"""

    # Build list of stations
    stations = build_station_list()

    #Values to try
    filter_radius = 10
    centre = (52.2053, 0.1218)
    station_list = stations_within_radius(stations, centre, filter_radius)

    #Find station 'Bin Brook' and assert it is found (known station within radius for values above - change if values to test are changed)
    station_to_find = "Bin Brook"
    for station in station_list:
        if station.name == station_to_find:
            station_bin_brook = station
            break
    assert station_bin_brook

    #Check all found stations are within radius
    for station in station_list:
        assert hav(station.coord, centre) < filter_radius
    

 



