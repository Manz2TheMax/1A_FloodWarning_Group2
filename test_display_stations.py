from display_stations import create_plot
from bokeh.models import GMapOptions
from bokeh.plotting import gmap

def test_create_plot():
    """Tests subroutine create_plot"""
    # Create plot
    plot = create_plot("API Key")

    # Assert that the output plot is a Google Maps plot
    assert isinstance(plot, type(gmap("API Key", GMapOptions())))
