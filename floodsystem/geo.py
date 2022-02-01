# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from tkinter.font import names
from .utils import sorted_by_key  # noqa
from haversine import haversine as hav  # haversine function for distance

def stations_by_distance(stations, p):
    """For a list of station objects (stations) and a coordinate tuple (p),
    returns a list of station and distance tuples sorted by distance."""

    # First a list of (station, distance) tuples is made
    # The list is then sorted by the "sort_by_key" function
    # Uses haversine function to calculate distance
    return sorted_by_key([(station, hav(station.coord, p)) for station in stations], 1)

def stations_within_radius(stations, centre, r):
    """For a list of station objects (stations) and a coordinate tuple (centre),
    returns a list of all the stations within in a radius r (in km) of the centre coordinate."""

    # List to compile stations within radius
    stations_within_radius = [] 

    for station in stations:
        # If station within radius, add to list
        # Distance calculated using haversine function
        if hav(station.coord, centre) < r:
            stations_within_radius.append(station)
    return stations_within_radius
        

