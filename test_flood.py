"""Unit tests for the flood module"""

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def test_stations_highest_rel_level():
    """Tests subroutine stations_highest_rel_level"""

    # Build list of stations and get water levels
    stations = build_station_list()
    update_water_levels(stations)

    # Retrieve N stations with highest relative water level
    N = 10
    highest_stations = stations_highest_rel_level(stations, N)

    # Assert that the correct number of stations retrieved
    assert len(highest_stations) == N

    #Assert relative water level of all stations is actual value
    for i in range(len(highest_stations)):
        assert highest_stations[i].relative_water_level() is not None

    #Assert relative water levels are in descending order
    for i in range(len(highest_stations) - 1):
        assert highest_stations[i].relative_water_level() >= highest_stations[i+1].relative_water_level()