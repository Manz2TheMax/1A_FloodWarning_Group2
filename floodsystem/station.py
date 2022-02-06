# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""
    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
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

def inconsistent_typical_range_stations(stations):
    """For a list of MonitoringStation objects (stations), returns a list of
    all the stations with inconsistent typical range data."""

    return [station for station in stations if station.typical_range_consistent() == False]
