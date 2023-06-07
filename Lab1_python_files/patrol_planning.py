from itertools import permutations
from aStar import distance_between 

def patrol_path(nodes):
    perms = list(permutations(nodes))
    distances = []
    for perm in perms:
        total_perm_distance = 0
        for i in range(len(perm) - 1):
            j = i + 1
            distance = distance_between(perm[i], perm[j])
            total_perm_distance += distance
        total_perm_distance += distance_between(perm[len(perm) - 1], perm[0])
        distances.append(total_perm_distance)

    index = 0
    min_dist = distances[0]
    for i in range(len(distances)):
        if(distances[i] < min_dist):
            min_dist = distances[i]
            index = i
    
    return perms[index]