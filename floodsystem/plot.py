"""This module provides tools for displaying water levels over time

"""

import matplotlib.pyplot as plt
from matplotlib import dates as date
from datetime import datetime, timedelta
from .analysis import polyfit

def prepare_water_levels_plot(current_plot, station, dates, levels):
    """For a MonitoringStation object (station), a list of dates (dates), a list of water levels (levels) and a plot,
    updates the plot to include a graph of the water level against time, as well as the typical range of values."""
    # Get the values for the low and high typical range
    low, high = station.typical_range

    # Check if the levels list has any terms and change labels accordingly
    if levels:
        current_plot.plot(dates, levels, label="Water Level")
    else:
        # If the list is empty, add the dates of the past 10 days to the "dates" list so the typical ranges
        # can be plotted
        dates = [datetime.today() - timedelta(days=x) for x in range(11)]
        current_plot.plot(dates, [None] * 11, label="Water Level - Value Not Found")

    # Check if the high typical value is "None" and change label accordingly
    if high is None:
        current_plot.plot(dates, [high] * len(dates), label="Typical High - Value Not Found")
    else:
        current_plot.plot(dates, [high] * len(dates), label="Typical High")

    # Check if the low typical value is "None" and change label accordingly
    if low is None:
        current_plot.plot(dates, [low] * len(dates), label="Typical Low - Value Not Found")
    else:
        current_plot.plot(dates, [low] * len(dates), label="Typical Low")

def plot_water_levels(station, dates, levels):
    """For a MonitoringStation object (station), a list of dates (dates) and a list of water levels (levels),
    displays a plot of the water level against time, as well as the typical range of values."""

    # Add the graphs for the station to the plot
    prepare_water_levels_plot(plt, station, dates, levels)

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

def plot_water_level_with_fit(station, dates, levels, p):
    """For a MonitoringStation object (object), a list of dates (dates) and a list of water levels (levels),
    displays a plot of the water level against time, as well as the best fit of the water level by a polynomial
    of degree p."""

    # Get the values for the low and high typical range
    low, high = station.typical_range

    # Check if the levels list has any terms and change labels accordingly
    if levels:

        #Obtain and plot polynomial expression (also calculate inputs for polynomial function)
        poly, d0 = polyfit(dates, levels, p)
        poly_x = date.date2num(dates) - d0
        plt.plot(dates, poly(poly_x), label="Water Level Best Fit")

        #Plot actual data
        plt.plot(dates, levels, label="Water Level")

    else:
        # If the list is empty, add the dates of the past 2 days to the "dates" list so the typical ranges
        # can be plotted
        dates = [datetime.today() - timedelta(days=x) for x in range(3)]
        plt.plot(dates, [None]*3, label="Water Level - Value Not Found")

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

def generalised_plot_water_levels(stations, dates, levels, *args, **kwargs):  # Extension Task
    """For a list of up to 6 MonitoringStation objects (stations),
    and their corresponding lists of dates (dates) and water levels (levels) and subplot arguments,
    displays a plot containing subplots of the water level against time and typical range of values for each station."""

    # Check if more than 6 stations are given
    if len(stations) > 6:
        raise ValueError(f"Only 6 stations can be plotted at once, {len(stations)} were given.")

    # Calculates the scale of the parent plot based on the number and location of the subplots
    if len(args) == 1:
        figure_size = (4, 4 * args[0])
    else:
        figure_size = (4 * args[1], 4 * args[0])

    # Create a plot and subplots
    fig, axs = plt.subplots(*args, **kwargs, figsize=figure_size)

    # Plot the station data based on the shape/location of the subplots
    dimensions = len(axs.shape)
    if dimensions == 1:
        for y in range(axs.shape[0]):
            # Add the graphs to the subplot
            prepare_water_levels_plot(axs[y], stations[y], dates[y], levels[y])
            # Add the name, legend and axis labels to the subplot
            axs[y].set_title(stations[y].name)
            axs[y].legend()
            axs[y].tick_params(labelrotation=45)  # Rotate dates by 45 degrees
            axs[y].set(xlabel='date', ylabel='water level (m)')
    else:
        height, length = axs.shape
        for y in range(height):
            for x in range(length):
                # Break the loop if all stations have been plotted
                if y * length + x == len(stations):
                    break
                # Add the graphs to the subplot
                prepare_water_levels_plot(axs[y, x], stations[y * length + x], dates[y * length + x],
                                          levels[y * length + x])
                # Add the name, legend and axis labels to the subplot
                axs[y, x].set_title(stations[y * length + x].name)
                axs[y, x].legend()
                axs[y, x].tick_params(labelrotation=45)  # Rotate dates by 45 degrees
                axs[y, x].set(xlabel='date', ylabel='water level (m)')

    fig.tight_layout()  # This makes sure plot does not cut off date labels

    # Show the plot
    fig.show()

