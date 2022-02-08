# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""
    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town, catchment):

        self._station_id = station_id
        self._measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self._name = label
        if isinstance(label, list):
            self._name = label[0]

        self._coord = coord
        self._typical_range = typical_range
        self._river = river
        self._town = town
        self._catchment = catchment

        self._latest_level = None



    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        d += "   typical range: {}".format(self.catchment_name)
        return d

    def typical_range_consistent(self):
        """This subroutine checks that the data for the typical low/high ranges for the station
        is consistent (i.e., the data is available, and the reported typical high range is above
        the reported typical low range). Returns True if consistent, False if not."""

        #Check that typical range exists - if it does not exist, return False
        if self.typical_range == None:
            return False

        # If reported typical high range is less than reported typical low, data is inconsistent (so return False)
        if self.typical_range[1] < self.typical_range[0]:
            return False

        # If all checks are passed, data is consistent (so returns True)
        return True

    def get_station_id(self):
        return self._station_id

    def set_station_id(self, value):
        self._station_id = value

    def del_station_id(self):
        del self._station_id

    def get_measure_id(self):
        return self._measure_id

    def set_measure_id(self, value):
        self._measure_id = value

    def del_measure_id(self):
        del self._measure_id

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    def get_coord(self):
        return self._coord

    def set_coord(self, value):
        self._coord = value

    def del_coord(self):
        del self._coord

    def get_typical_range(self):
        return self._typical_range

    def set_typical_range(self, value):
        self._typical_range = value

    def del_typical_range(self):
        del self._typical_range

    def get_river(self):
        return self._river

    def set_river(self, value):
        self._typical_range = value

    def del_river(self):
        del self._river

    def get_town(self):
        return self._town

    def set_town(self, value):
        self._town = value

    def del_town(self):
        del self._town

    def get_latest_level(self):
        return self._latest_level

    def set_latest_level(self, value):
        self._latest_level = value

    def del_latest_level(self):
        del self._latest_level

    def get_catchment(self):
        return self._catchment_name

    def set_catchment(self, value):
        self._catchment_name = value

    def del_catchment(self):
        del self._catchment_name

    station_id = property(get_station_id, set_station_id, del_station_id, "Station ID")
    measure_id = property(get_measure_id, set_measure_id, del_measure_id, "Measure ID")
    name = property(get_name, set_name, del_name, "Name")
    coord = property(get_coord, set_coord, del_coord, "Coordinates")
    typical_range = property(get_typical_range, set_typical_range, del_typical_range, "Typical range")
    river = property(get_river, set_river, del_river, "River")
    town = property(get_town, set_town, del_town, "Town")
    latest_level = property(get_latest_level, set_latest_level, del_latest_level, "Latest level")
    catchment = property(get_catchment, set_catchment, del_catchment, "Catchment")


def inconsistent_typical_range_stations(stations):
    """For a list of MonitoringStation objects (stations), returns a list of
    all the stations with inconsistent typical range data."""

    return [station for station in stations if station.typical_range_consistent() == False]
