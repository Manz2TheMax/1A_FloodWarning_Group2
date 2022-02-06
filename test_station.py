# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """Tests subroutine typical_range_consistent"""

    #Default values to use for station object
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    river = "River X"
    town = "My Town"

    # Check one - returns true for consistent value
    trange_1 = (-1.0, 1.0)
    s = MonitoringStation(s_id, m_id, label, coord, trange_1, river, town)
    assert s.typical_range_consistent() == True

    # Check two - returns true if high and low values are equal
    trange_2 = (1.0, 1.0)
    s.typical_range = trange_2
    assert s.typical_range_consistent() == True

    # Check three - returns false if high value is less than low value
    trange_3 = (1.0, -1.0)
    s.typical_range = trange_3
    assert s.typical_range_consistent() == False

    # Check four - returns false if no typical range data available
    trange_4 = None
    s.typical_range = trange_4
    assert s.typical_range_consistent() == False
    

def test_inconsistent_typical_range_stations():

    #Retrieve list of stations
    all_station_list = build_station_list()
    inconsistent_station_list = inconsistent_typical_range_stations(all_station_list)

    #For each station, check if correctly put or not put in list of inconsistent stations
    for station in all_station_list:
        if station in inconsistent_station_list:
            assert station.typical_range_consistent() == False
        else:
            assert station.typical_range_consistent() == True
        

