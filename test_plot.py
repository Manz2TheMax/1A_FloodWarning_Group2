"""Unit tests for the plot module"""

from floodsystem.station import MonitoringStation
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta


def test_plot_water_levels():
    """Tests subroutine plot_water_levels"""

    # Create a function that checks for exceptions. Returns "True" if no exceptions have been raised
    def check_for_errors(function, *args):
        try:
            function(*args)
            return True
        except:
            return False

    # Create lists of dates and test values
    dates = [datetime.today() - timedelta(days=x) for x in range(10)]
    levels = [0, 1] * 5

    # Create a station with values for typical low and high
    test_station = MonitoringStation(None, None, None, None, (0, 1), None, None, None)
    # Assert the function runs without errors for numerical values of typical low, high and water levels
    assert check_for_errors(plot_water_levels, test_station, dates, levels) is True

    # Assert the function runs without errors for "None" as the water level
    assert check_for_errors(plot_water_levels, test_station, None, None) is True

    # Set typical high to "None"
    test_station.typical_range = (0, None)
    # Assert the function runs without errors for "None" as the typical high value
    assert check_for_errors(plot_water_levels, test_station, dates, levels) is True

    # Set typical low to "None"
    test_station.typical_range = (None, 1)
    # Assert the function runs without errors for "None" as the typical low value
    assert check_for_errors(plot_water_levels, test_station, dates, levels) is True

    # Set typical low and high to "None"
    test_station.typical_range = (None, None)
    # Assert the function runs without errors for "None" as all values
    assert check_for_errors(plot_water_levels, test_station, None, None) is True
