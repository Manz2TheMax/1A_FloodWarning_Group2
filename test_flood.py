"""Unit tests for the flood module"""

from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import get_flood_risk_rating, get_level_rise, get_station_flood_risk, stations_highest_rel_level
from floodsystem.flood import stations_level_over_threshold
from floodsystem.flood import get_town_flood_risk
from floodsystem.geo import stations_by_town
from floodsystem.station import MonitoringStation
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta

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

def test_get_station_flood_risk():
    assert 0 == 0

def test_get_station_flood__risk():
    """Tests subroutine get_station_flood_risk"""

    # Build list of stations and get water (will test first station)
    stations = build_station_list()
    update_water_levels(stations)
    station_to_test = stations[0]

    #Get station risk, relative water level, and level rise for station
    station_risk = get_station_flood_risk(station_to_test)
    rel_water_level = station_to_test.relative_water_level()
    level_rise = get_level_rise(station_to_test)

    #Ensure given relative water level and level rise gives correct result
    if rel_water_level > 2 and level_rise > 0.1:
        assert station_risk == 4
    elif rel_water_level > 2 and level_rise < 0:
        assert station_risk == 2
    elif rel_water_level > 2:
        assert station_risk == 3
    elif rel_water_level < 2 and level_rise > 0.1:
        assert station_risk == 2
    elif rel_water_level < 2 and level_rise < 0:
        assert station_risk == 0
    else:
        assert station_risk == 1

def test_get_level_rise():
    """Tests subroutine get_level_rise"""

    # Build list of stations and get water
    stations = build_station_list()
    update_water_levels(stations)

    #Assert that when no data found, level rise is None
    for i in range(20):
        level_rise = get_level_rise(stations[i])
        times, values = fetch_measure_levels(stations[i].measure_id, timedelta(days=2))
        if (times or values) == False:
            assert level_rise == None

def test_get_town_flood_risk():
    """Tests subroutine get_town_flood_risk"""

    # Build list of stations and get water
    stations = build_station_list()
    update_water_levels(stations)

    #Get list of time and choose first town to test
    towns = stations_by_town(stations)
    town_to_test = list(towns.keys())[0]

    town_flood_risk = get_town_flood_risk(town_to_test, towns) #Get town flood risk

    #Assert risks of each station do not exceed town risk, and that town risk is same as maximum station risk
    max_risk = 0
    for station in towns[town_to_test]:
        station_risk = get_station_flood_risk(station)
        assert station_risk <= town_flood_risk
        if station_risk > max_risk:
            max_risk = station_risk
    assert max_risk == town_flood_risk


def test_get_flood_risk_rating():
    """Tests subroutine flood_risk_rating"""

    assert get_flood_risk_rating(0) == "Low"
    assert get_flood_risk_rating(1) == "Low"
    assert get_flood_risk_rating(2) == "Moderate"
    assert get_flood_risk_rating(3) == "High"
    assert get_flood_risk_rating(4) == "Severe"
    assert get_flood_risk_rating(None) == None
    assert get_flood_risk_rating(5) == None
