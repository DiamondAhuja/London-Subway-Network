from Itinerary import *


def distance_between(station1, station2):
    # approximate radius of earth in km
    R = 6373.0

    lat1 = radians(station1.get_lat())
    lon1 = radians(station1.get_long())
    lat2 = radians(station2.get_lat())
    lon2 = radians(station2.get_long())

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def index_finder(stations, id):
    for station in stations:
        if station[0] == id:
            return station


def all_paths_distances(stations, all_paths):
    path_distances = []

    for i in range(len(all_paths)):
        distance = 0
        for j in range(len(all_paths[i]) - 1):
            station1 = index_finder(stations, all_paths[i][j])
            station2 = index_finder(stations, all_paths[i][j + 1])
            distance += distance_between(station1, station2)
        path_distances.append(distance)
    return path_distances


def find_all_paths(dict, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in dict:
        return []
    paths = []
    for node in dict[start]:
        if node not in path:
            newpaths = find_all_paths(dict, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def get_shortest(path_distances, all_paths):
    min_value = min(path_distances)
    index = path_distances.index(min_value)
    return all_paths[index]
