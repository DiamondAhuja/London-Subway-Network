from Graph import *
from Station import *
from benchmarking import *


def read_input(input_stream):
    data = []
    for line in input_stream.readlines():
        line = line.strip("\n")
        data.append(list(line.split(",")))
    return data


def station_data(data_set):
    id = data_set[0].index('"id"')
    name = data_set[0].index('"name"')
    lat = data_set[0].index('"latitude"')
    long = data_set[0].index('"longitude"')
    zone = data_set[0].index('"zone"')
    rail = data_set[0].index('"id"')
    lines = data_set[0].index('"total_lines"')
    return id, lat, long, name, zone, lines, rail


def connections_data(data_set):
    station1 = data_set[0].index('"station1"')
    station2 = data_set[0].index('"station2"')
    time = data_set[0].index('"time"')
    line = data_set[0].index('"line"')
    return [station1, station2, line, time]


def build_stations(data_set):
    stations = []
    id_ix, lat_ix, long_ix, name_ix, zone_ix, lines_ix, rail_ix = station_data(data_set)
    for i in range(1, len(data_set)):
        s = Station(data_set[i][id_ix], data_set[i][lat_ix], data_set[i][long_ix], data_set[i][name_ix],
                    data_set[i][zone_ix], data_set[i][lines_ix], data_set[i][rail_ix])
        stations.append(s)
    return stations


def create_keys(data_set):
    dict = {}
    data = connections_data(data_set)
    station_id, connection_id = data[0], data[1]
    for i in range(1, len(data_set)):
        dict[data_set[i][station_id]] = {}
        dict[data_set[i][connection_id]] = {}
    return dict


def create_weighted_connections(data_set):
    data = connections_data(data_set)
    station_id, connection_id, weight = data[0], data[1], data[3]

    dict = create_keys(data_set)

    for key in dict:
        for i in range(1, len(data_set)):
            current_vertex = (data_set[i][station_id])
            neighbour = (data_set[i][connection_id])
            current_weight = int(data_set[i][weight])
            if current_vertex == key:
                dict[key].update({neighbour: current_weight})
            elif neighbour == key:
                dict[key].update({current_vertex: current_weight})
    return dict


def main():
    f = open("C:/Users/diamo/OneDrive - McMaster University/3rd Year (Sep 2022 - April 2023)/First Semester (Fall)/SFWRENG 3XB3 - Binding Theory to Practice/Lab 1/l1-graph-lab/_dataset/london.connections.csv", "r")
    data = (read_input(f))
    dict = (create_weighted_connections(data))
    G = Graph(dict)
    dijkstra_iterations(G)
    create_plot()


main()
