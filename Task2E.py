from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.plot import plot_water_levels


def run():
    """Requirements for Task 2E"""

    # Build a list of stations
    stations = build_station_list()
    # Update the water level so the latest level is included
    update_water_levels(stations)

    # Plot the water level graph for 5 stations with the largest relative water levels
    for station in stations_highest_rel_level(stations, 5):
        # Get the values of time and water level for the past 10 days
        times, values = fetch_measure_levels(station.measure_id, timedelta(days=10))
        # Plot the graph
        plot_water_levels(station, times, values)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()
