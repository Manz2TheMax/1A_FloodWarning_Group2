"""Unit test for the geo module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius
from floodsystem.geo import rivers_by_station_number
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_by_river
from floodsystem.geo import rivers_with_station
from haversine import haversine as hav  # haversine function for distance

def test_stations_within_radius():
    """Tests subroutine stations_within_radius"""

    # Build list of stations
    stations = build_station_list()

    #Values to try
    filter_radius = 10
    centre = (52.2053, 0.1218)
    station_list = stations_within_radius(stations, centre, filter_radius)

    #Find station 'Bin Brook' and assert it is found (known station within radius for values above - change if values to test are changed)
    station_to_find = "Bin Brook"
    for station in station_list:
        if station.name == station_to_find:
            station_bin_brook = station
            break
    assert station_bin_brook

    #Check all found stations are within radius
    for station in station_list:
        assert hav(station.coord, centre) < filter_radius

def test_rivers_by_station_number():
    """Tests subroutine rivers_by_station_number"""
    
    # Build list of stations
    stations = build_station_list()

    #N is the number of entries to find as input to the subroutine
    N = 11
    output = rivers_by_station_number(stations, N)

    #Assert correct value of N (= length of list minus number of additional entries at end with same number of stations)
    n_used = len(output)
    i = len(output) - 1
    while output[i][1] == output[i-1][0]:
        n_used -= 1
        i -= 1
    assert n_used == N

    #Assert rivers are output in order of decreasing number of stations
    for i in range(len(output) - 1):
        assert output[i][1] >= output[i+1][1]

    #Assert that, if there are more than N entries, the additional entries have the same number of stations as the Nth entry
    if N > len(output):
        for i in range(N, len(output)):
            assert output[N-1][0] == output[i][0]

    #Assert that next river after last river in output list has less stations than the last river in output list
    #Generate another output with more rivers
    next_output = rivers_by_station_number(stations, len(output) + 1)
    #Assert that there are more rivers in second output
    assert len(next_output) > len(output)
    #Assert that first river not in original output less has less stations than the last river in the first output list
    assert next_output[len(output)][1] < output[len(output) - 1][1]


def test_stations_by_distance():
    """Tests subroutine stations_by_distance"""

    # Build list of stations
    stations = build_station_list()

    # Build list of stations and their corresponding distances
    sorted_stations = stations_by_distance(stations, (52.2053, 0.1218))

    # Assert that the stations are in order of increasing distance
    for index in range(len(sorted_stations) - 1):
        assert sorted_stations[index][1] <= sorted_stations[index + 1][1]

    # List of the 10 closest stations to Cambridge city centre
    known_closest_stations = [('Cambridge Jesus Lock', 'Cambridge', 0.8402364350834995),
                              ('Bin Brook', 'Cambridge', 2.502274086951454),
                              ("Cambridge Byron's Pool", 'Grantchester', 4.0720438555077125),
                              ('Cambridge Baits Bite', 'Milton', 5.115589516578674),
                              ('Girton', 'Girton', 5.227070345811418),
                              ('Haslingfield Burnt Mill', 'Haslingfield', 7.044388165868453),
                              ('Oakington', 'Oakington', 7.128249171700346),
                              ('Stapleford', 'Stapleford', 7.265694306995238),
                              ('Comberton', 'Comberton', 7.7350743760373675),
                              ('Dernford', 'Great Shelford', 7.993861351711722)]

    # Store the 10 closest stations in the same format at the known ones
    calculated_closest_stations = [(station[0].name, station[0].town, station[1]) for station in sorted_stations[:10]]

    # Check if the calculated closest stations are the same as the known ones
    for known, calculated in zip(known_closest_stations, calculated_closest_stations):
        # Assert that calculated stations and known stations have the same name
        assert known[0] == calculated[0]
        # Assert that calculated stations and known stations are on the same river
        assert known[1] == calculated[1]
        # Assert the difference in distance is less than or equal to one meter
        assert abs(known[2] - calculated[2]) * 1000 <= 1

    # List of the 10 furthest stations from Cambridge city centre
    known_furthest_stations = [('Boscadjack', 'Wendron', 440.0026482838576),
                               ('Gwithian', 'Gwithian', 442.05491558132354),
                               ('Helston County Bridge', 'Helston', 443.37824966454974),
                               ('Loe Pool', 'Helston', 445.07184458260684),
                               ('Relubbus', 'Relubbus', 448.64944322554413),
                               ('St Erth', 'St Erth', 449.03415711886015),
                               ('St Ives Consols Farm', 'St Ives', 450.0734690482922),
                               ('Penzance Tesco', 'Penzance', 456.3857579793324),
                               ('Penzance Alverton', 'Penzance', 458.5766422710278),
                               ('Penberth', 'Penberth', 467.53367291629183)]

    # Store the 10 furthest stations in the same format at the known ones
    calculated_furthest_stations = [(station[0].name, station[0].town, station[1]) for station in sorted_stations[-10:]]

    # Check if the calculated closest stations are the same as the known ones
    for known, calculated in zip(known_furthest_stations, calculated_furthest_stations):
        # Assert that calculated stations and known stations have the same name
        assert known[0] == calculated[0]
        # Assert that calculated stations and known stations are on the same river
        assert known[1] == calculated[1]
        # Assert the difference in distance is less than or equal to one meter
        assert abs(known[2] - calculated[2]) * 1000 <= 1


def test_rivers_with_station():
    """Tests subroutine rivers_with_station"""

    # Build list of stations
    stations = build_station_list()

    # Create list of rivers with least one monitoring station
    river_names = list(rivers_with_station(stations))

    # List of known rivers with at least one monitoring station
    known_rivers = ['Addlestone Bourne', 'River Adur', 'Aire Washlands', 'Alconbury Brook',
                    'Aller Brook', 'River Alre', 'River Alt', 'Alverthorpe Beck', 'Ampney Brook']

    # Assert that the known rivers are in the output of the function
    for river in known_rivers:
        assert river in river_names

    # List of all monitoring stations on river Cam
    cam_stations = [station for station in stations if station.river == "River Cam"]

    # Assert that the output does not include duplicate names
    assert rivers_with_station(cam_stations) == {"River Cam"}


def test_stations_by_river():
    """Tests subroutine stations_by_river"""

    # Build list of stations
    stations = build_station_list()

    # Dictionary containing river names and their corresponding stations
    rivers = stations_by_river(stations)

    # Create lists of stations on rivers Aire, Cam and Thames
    stations_on_aire = [station.name for station in rivers["River Aire"]]
    stations_on_cam = [station.name for station in rivers["River Cam"]]
    stations_on_thames = [station.name for station in rivers["River Thames"]]

    # Create a list containing the lists above
    all_stations = [stations_on_aire, stations_on_cam, stations_on_thames]

    # Dictionary containing lists of some known stations on rivers Aire, Cam and Thames
    known_stations = {"River Aire":
                      ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley',
                       'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley'],
                      "River Cam":
                      ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford',
                       'Weston Bampfylde'],
                      "River Thames":
                      ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock',
                       'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade']}

    # Assert that for each river, the known stations are in the output of the function
    for known_list, output_list in zip(known_stations.values(), all_stations):
        for known_station in known_list:
            assert known_station in output_list
