"""This module contains subroutines that allow station levels to be analysed."""

from matplotlib import dates as date
import numpy as np

def polyfit(dates, levels, p):
    """For a given set of dates and levels for a station, obtains a polynomial approximation of the curve
    (change in level with respect to time). The polynomial will be of degree p. Please note that the first
    data point in the list will be treated as x=0 (vertical intercept) - d0 is the offset of the horizontal 
    axis as a result."""

    #Convert dates to values 
    x = date.date2num(dates)

    #Calculate offset of dates (first date treated as 0 point)
    d0 = x[0]

    #Calculate polynomial (using offset d0) and convert to numpy.poly1d object
    p_coeff = np.polyfit(x - d0, levels, p)
    poly = np.poly1d(p_coeff)

    #Return polynomial and offset
    return poly, d0
