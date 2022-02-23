from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.plot import plot_water_levels

def run():
    """Requirements for Task 2F"""

    # Build a list of stations
    stations = build_station_list()
    # Update the water level so the latest level is included    
    update_water_levels(stations)

    # Plot the water level graph for 5 stations with the largest relative water levels
    for station in stations_highest_rel_level(stations, 5):
        # Get the values of time and water level for the past 2 days
        times, values = fetch_measure_levels(station.measure_id, timedelta(days=2))
        # Plot the graph (use polynomial degree of 4)
        plot_water_level_with_fit(station, times, values, p=4)



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
