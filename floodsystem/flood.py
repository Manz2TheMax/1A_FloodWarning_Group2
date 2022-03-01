"""This module provides tools for assessing flood risk
"""

from datetime import timedelta
from floodsystem.datafetcher import fetch_measure_levels
import numpy as np
from floodsystem.analysis import polyfit
from matplotlib import dates as date

def stations_level_over_threshold(stations, tol):
    """For a list of MonitoringStation objects (stations) and a tolerance value (tol),
    returns a list of tuples containing a MonitoringStation object and its corresponding relative water level.
    The returned list is sorted by the relative level in descending order.

    Note: "update_water_levels" function needs to be called at least once for this function to work."""

    # Create the output list
    output = []

    for station in stations:
        # Get the relative water level. Will be "None" if typical range is inconsistent or the latest level
        # is not known
        relative_level = station.relative_water_level()

        # Check if the relative level is "None" and, if not "None", compare it with the tolerance value
        if relative_level is not None and relative_level > tol:
            # Append tuple of MonitoringStation object and relative level to the output list
            output.append((station, relative_level))

    # Sort the list in order of descending relative water levels
    output.sort(key=lambda val: val[1], reverse=True)

    # Return the output list
    return output

def stations_highest_rel_level(stations, N):
    """For a list of MonitoringStaton objects (stations), returns a list of the N stations
    at which the water level, relative to the typical range, is highest"""

    #Filter list as to not include stations without relative water level
    new_stations = list(filter(lambda station: station.relative_water_level() is not None, stations))

    #Sorts stations in descending order of relative water level
    new_stations.sort(key=lambda station: station.relative_water_level(), reverse = True)

    #Return first N stations in lists (N stations with highest water level)
    return new_stations[:N]

def get_station_flood_risk(station):
    """For a MonitoringStation object (station), returns flood a risk rating - a number between 
    0 and 4. Uses data for the relative water level and the rise in the """

    flood_risk = 0

    rel_level_threshold = 2
    rise_threshold = 0.1
    
    #First factor is the current relative water level of station - sets initial risk 
    rel_water_level = station.relative_water_level()

    #If no data available for relative water level, cannot calculate score, so return None
    if rel_water_level is None:
        return None
    if rel_water_level > rel_level_threshold:
        flood_risk = 3 #If above threshold, set high risk
    else:
        flood_risk = 1 #If below threshold, set low risk

    #Second factor is the rate of change of the water level (e.g., if rising rapidly, give a high score) - used to adjust risk
    level_rise = get_level_rise(station)

    #If no data available for level rise, cannot calculate score, so return None
    if level_rise is None:
        return None

    #For decreasing level, reduce flood risk
    if level_rise < 0:
        flood_risk -= 1
    #For increasing level above threshold, increase flood risk
    if level_rise > rise_threshold:
        flood_risk += 1

    return flood_risk

def get_level_rise(station):
    """For a MonitoringStation object (station), returns a the rate of water level rise, specifically
    the average value over the last 2 days"""
    #Fetch data (if no data available, return None)
    times, values = fetch_measure_levels(station.measure_id, timedelta(days=2))
    
    #Only continue if data available, otherwise return None
    if times and values and     (None in times or None in values) == False:
        #Get polynomial approximation of
        poly, d0 = polyfit(times, values, p=4)

        #Find derivative polynomial
        level_der = np.polyder(poly)
        
        #Obtain list of gradients over last 2 days using the derivative polynomial
        grads = []
        for t in times:
            grads.append(level_der(date.date2num(t) - d0))

        #Return average of gradient values
        return np.average(grads)
    else:
        return None

def get_town_flood_risk(town, stations_by_town):
    """Obtains the flood risk for a town, based on the flood risks for the towns
    respective station, using the same rating system - returned value is the highest
    flood risk of the towns stations"""
    
    #Get stations for town
    stations_in_town = stations_by_town[town]

    flood_risk = get_station_flood_risk(stations_in_town[0])
    
    #Find highest flood risk value from town's stations by iterating through stations
    for i in range(1, len(stations_in_town)):
        new_flood_risk = get_station_flood_risk(stations_in_town[i])
        if new_flood_risk is None:
            break
        if flood_risk is None or new_flood_risk > flood_risk:
            flood_risk = new_flood_risk
    
    #Return highest value
    return flood_risk

def get_flood_risk_rating(num):
    """Converts an integer value of a flood risk rating to the rating it 
    represents - low (0/1), moderate (2), high (3), severe (4)"""

    if num == 0 or num == 1:
        return "Low"
    if num == 2:
        return "Moderate"
    if num == 3:
        return "High"
    if num == 4:
        return "Severe"
    return None #default (for None value or other)

