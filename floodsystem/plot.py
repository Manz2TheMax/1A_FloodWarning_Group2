"""This module provides tools for displaying water levels over time

"""

import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_water_levels(station, dates, levels):
    """For a MonitoringStation object (object), a list of dates (dates) and a list of water levels (levels),
    displays a plot of the water level against time, as well as the typical range of values."""

    # Get the values for the low and high typical range
    low, high = station.typical_range

    # Check if the levels list has any terms and change labels accordingly
    if levels:
        plt.plot(dates, levels, label="Water Level")
    else:
        # If the list is empty, add the dates of the past 10 days to the "dates" list so the typical ranges
        # can be plotted
        dates = [datetime.today() - timedelta(days=x) for x in range(11)]
        plt.plot(dates, [None]*11, label="Water Level - Value Not Found")

    # Check if the high typical value is "None" and change label accordingly
    if high is None:
        plt.plot(dates, [high] * len(dates), label="Typical High - Value Not Found")
    else:
        plt.plot(dates, [high] * len(dates), label="Typical High")

    # Check if the low typical value is "None" and change label accordingly
    if low is None:
        plt.plot(dates, [low] * len(dates), label="Typical Low - Value Not Found")
    else:
        plt.plot(dates, [low] * len(dates), label="Typical Low")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    # Add a legend to the graph and show the plot
    plt.legend()
    plt.show()