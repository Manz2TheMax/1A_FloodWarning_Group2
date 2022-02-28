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
    """For a list of MonitoringStation objects (stations) and a coordinate tuple (p),
    returns a list of station and distance tuples sorted by distance."""

    # First a list of (station, distance) tuples is made
    # The list is then sorted by the "sort_by_key" function
    # Uses haversine function to calculate distance
    return sorted_by_key([(station, hav(station.coord, p)) for station in stations], 1)


def stations_within_radius(stations, centre, r):
    """For a list of MonitoringStation objects (stations) and a coordinate tuple (centre),
    returns a list of all the stations within in a radius r (in km) of the centre coordinate."""

    # List to compile stations within radius
    stations_within_radius = []

    for station in stations:
        # If station within radius, add to list
        # Distance calculated using haversine function
        if hav(station.coord, centre) < r:
            stations_within_radius.append(station)
    return stations_within_radius


def stations_by_river(stations):
    """For a list of MonitoringStation objects (stations),
    returns a dictionary that maps river names (key) to a list of MonitoringStation objects on a given river."""

    # Dictionary containing river names and their corresponding stations
    rivers = {}

    for station in stations:
        # Check if river is already in the dictionary
        if station.river in rivers:
            # Check if the station has already been added to the list
            if station not in rivers[station.river]:
                rivers[station.river].append(station)

        else:
            rivers.update({station.river: [station]})

    return rivers


def rivers_with_station(stations):
    """For a list of MonitoringStation objects (stations),
    returns a set object containing the names of the rivers monitored by the given stations."""

    # Set with the river names. Using "set" objects prevents duplicate names.
    rivers = set()

    for station in stations:
        # Add name to set
        rivers.add(station.river)

    return rivers

def rivers_by_station_number(stations, N):
    """For a list of MonitoringStation objects (stations), returns a list of 
    tuples (river name, number of stations) of the names of the N rivers with 
    the greatest number of stations, sorted by their number of stations.
    Note that, if there are more rivers with the same number of stations as the 
    Nth entry, these rivers will be included in the list."""

    # Obtain dictionary of rivers with list of monitoring stations for each river
    rivers = stations_by_river(stations)

    # Sort rivers by number of stations (in descending order)
    sorted_rivers = sorted(rivers.items(), key=lambda k: len(k[1]), reverse = True)

    # List of tuples to return
    rivers_and_station_num = []

    i = 0
    #Add tuples to list for first N items and from then on if number of stations equal to that of the Nth entry
    #'i != 0 term' means it is not checked on first iteration which would throw error as no item previous to 0th index
    while i < N or (i != 0 and len(sorted_rivers[i-1][1]) == len(sorted_rivers[i][1])):
        rivers_and_station_num.append((sorted_rivers[i][0], len(sorted_rivers[i][1])))
        i += 1
    
    return rivers_and_station_num

def stations_by_town(stations):
    """For a list of MonitoringStation objects (stations),
    returns a dictionary that maps town names (key) to a list of MonitoringStation objects on a given town."""

    # Dictionary containing town names and their corresponding stations
    towns = {}

    for station in stations:
        # Check if town is already in the dictionary
        if station.town in towns:
            # Check if the station has already been added to the list
            if station not in towns[station.town]:
                towns[station.town].append(station)

        else:
            towns.update({station.town: [station]})

    return towns


    