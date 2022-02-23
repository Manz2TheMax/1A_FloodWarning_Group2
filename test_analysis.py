"""Unit tests for analysis module"""

from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from matplotlib import dates as date

def test_analysis():
    stations = build_station_list()
    # Update the water level so the latest level is included    
    update_water_levels(stations)
    
    #Test for 10 stations in list
    for i in range(10):
        times, values = fetch_measure_levels(stations[i].measure_id, timedelta(days=2))
        numtimes = date.date2num(times)

        #Use degree 5 for polyfit
        poly, d0 = polyfit(times, values, p=5)

        #Tolerance for how close actual values should be with values from polynomial
        tol = 1

        for i in range(len(times)):
            #Assert all polynomial values are within tolerance
            assert abs(poly(numtimes[i] - d0) - values[i]) < tol