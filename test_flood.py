"""Unit tests for the flood module"""

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation

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

def test_stations_level_over_threshold():
    """Tests subroutine stations_level_over_threshold"""

    # Build list of stations and get water
    stations = build_station_list()
    update_water_levels(stations)

    # Get a list of all stations with relative water level above 0.8
    over_threshold = stations_level_over_threshold(stations, 0.8)

    # Create two stations with relative water level over 1
    test_station_1 = MonitoringStation(None, None, None, None, (0, 1), None, None, None)
    test_station_1._latest_level = 128

    test_station_2 = MonitoringStation(None, None, None, None, (2, 3), None, None, None)
    test_station_2._latest_level = 256

    # Create a station with relative water level less than 1
    test_station_3 = MonitoringStation(None, None, None, None, (4, 5), None, None, None)
    test_station_3._latest_level = 1

    # Create a list of example monitoring stations
    test_stations = [test_station_1, test_station_2, test_station_3]
    # Assert the correct number of stations is returned
    assert len(stations_level_over_threshold(test_stations, 1)) == 2

    # Assert the relative water level is a number (float)
    for station in over_threshold:
        assert isinstance(station[1], float)

    # Assert the stations are in descending order of relative water levels
    for index in range(1, len(over_threshold)):
        assert over_threshold[index][1] <= over_threshold[index - 1][1]

    # Create a monitoring station without a numerical value for the latest level
    test_station_4 = MonitoringStation(None, None, None, None, (4, 5), None, None, None)
    test_station_4._latest_level = None

    # Assert the function does not crash if no stations are over the threshold or no latest level is given
    assert stations_level_over_threshold([test_station_3, test_station_4], 512) == []
