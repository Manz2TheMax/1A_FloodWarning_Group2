"""This module provides tools for assessing flood risk

"""

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
