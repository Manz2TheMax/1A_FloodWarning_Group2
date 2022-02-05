"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station_number
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

def test_rivers_by_station_number():
    """Tests subroutine rivers_by_station_number"""
    
    # Build list of stations
    stations = build_station_list()

    #N is the number of entries to find as input to the subroutine
    N = 11
    output = rivers_by_station_number(stations, N)

    #Assert correct value of N (= length of list minus number of additional entries at end with same number of stations)
    n_used = len(output)
    i = len(output) - 1
    while output[i][1] == output[i-1][0]:
        n_used -= 1
        i -= 1
    assert n_used == N

    #Assert rivers are output in order of decreasing number of stations
    for i in range(len(output) - 1):
        assert output[i][1] >= output[i+1][1]

    #Assert that, if there are more than N entries, the additional entries have the same number of stations as the Nth entry
    if N > len(output):
        for i in range(N, len(output)):
            assert output[N-1][0] == output[i][0]

    #Assert that next river after last river in output list has less stations than the last river in output list
    #Generate another output with more rivers
    next_output = rivers_by_station_number(stations, len(output) + 1)
    #Assert that there are more rivers in second output
    assert len(next_output) > len(output)
    #Assert that first river not in original output less has less stations than the last river in the first output list
    assert next_output[len(output)][1] < output[len(output) - 1][1]

    

 



