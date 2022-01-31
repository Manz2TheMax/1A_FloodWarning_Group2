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
    return sorted_by_key([(station, hav(station.coord, p)) for station in stations], 1)

def stations_within_radius(stations, centre, r):
    """For a list of station objects (stations) and a coordinate tuple (centre),
    returns a list of all the stations within in a radius r (in km) of the centre coordinate."""
    
    #Obtain list of stations sorted by distance - list of tuples, with only name of station and distance to coordinate centre
    station_distances = stations_by_distance(stations, centre)

    #List to compile names of stations within radius
    names_within_radius = [] 

    for i in range(len(station_distances)):
        #If station within radius, add name to list
        if station_distances[i][1] < r: 
            names_within_radius.append(station_distances[i][0].name)
        #Otherwise, no more stations to be added (as the rest of the stations will be outside
        #the radius as the list is sorted by distance), so exit for loop
        else: 
            break
    return names_within_radius
        

