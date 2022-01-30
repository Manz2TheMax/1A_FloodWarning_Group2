# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine as hav  # haversine function for distance

def stations_by_distance(stations, p):
    """For a list of station objects (stations) and a coordinate tuple (p),
    returns a list of station and distance tuples sorted by distance."""

    # First a list of (station, distance) tuples is made
    # The list is then sorted by the "sort_by_key" function
    return sorted_by_key([(station, hav(station.coord, p)) for station in stations], 1)
