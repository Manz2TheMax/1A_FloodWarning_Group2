from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool
from bokeh.plotting import gmap
from floodsystem.stationdata import build_station_list

# Stores the data required by the plot and Google maps
output_file("gmap.html")

# Configure the map
map_options = GMapOptions(lat=52.561928, lng=-1.464854, map_type="roadmap", zoom=6)

# For GMaps to function, Google requires you obtain and enable an API key:
# https://developers.google.com/maps/documentation/javascript/get-api-key

google_api_key = input("Please enter your personal Google API Key:\n")
# Create a GMap plot
p = gmap(google_api_key, map_options, title="England")

# Build stations list
stations = build_station_list()

# Separate the data required for the plot into individual lists
source = ColumnDataSource(
    data=dict(lat=[station.coord[0] for station in stations],
              lon=[station.coord[1] for station in stations],
              name=[station.name for station in stations],
              river=[station.river for station in stations])
)

# Show the name of the station and the river it is monitoring when hovering over the station
p.add_tools(HoverTool(tooltips=[("Name", "@name"), ("River", "@river")]))
# Show a blue circle for each station
p.circle(x="lon", y="lat", size=10, fill_color="blue", fill_alpha=0.25, source=source)

# Display the plot (will open a new browser tab)
show(p)
