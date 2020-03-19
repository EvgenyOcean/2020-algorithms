from collections import ChainMap

class PathFindingMistake(Exception): 
    def __str__(self):
        return 'Wrong graph representation. The path is unreachable or there\'s no path!'

paths = {
    'S': [{'A': 2}, {'B': 5}],
    'A': [{'AB': 3}],
    'B': [{'AB': 7}],
    'AB': [{'A1': 4, 'B1': 7}],
    'A1': [{'F': 100}],
    'B1': [{'B2': 7}],
    'B2': [{'C1': 2, 'B3': 8}],
    'C1': [],
    'B3': [{'F': 9}],
}

def find_fastest(paths, start, finish):
    costs = ChainMap() 
    try: #if paths is empty
        [costs.update({node: [value, [start]]}) for cost in paths[start] for (node,value) in cost.items()] #all code is garbage (c) TechLead :D
    except Exception: 
        raise PathFindingMistake
    done = [start]

    def least_cost(): #find the least 'expensive' path and return its name
        min_node = None
        min_value = float('inf')
        for node, value in costs.items(): 
            if value[0] < min_value and node not in done:
                min_value = value[0]
                min_node = node #'B'
        if min_node == None: return None #if nothing, then you checked everything and haven't reached the desired destination
        return min_node

    the_least = least_cost() #'B'
    while finish != the_least and the_least != None: 
        if paths[the_least]: #ONLY! if the node leads to other nodes
            for next_node in paths[the_least]: #
                for node, value in next_node.items(): 
                    if node in costs: #if this node already reached
                        if value + costs[the_least][0] < costs[node][0]: #and if there's faster way to this node
                            costs[node] = [value + costs[the_least][0], [*costs[the_least][1], the_least]] #(finding the fastest path and rewriting how we got here, basically, to keep the track of parents)
                    else:
                        costs.update({node: [value + costs[the_least][0], [*costs[the_least][1], the_least]]}) #new node has been reached, put it down
        #1. avoid double checking a node if its nodes were already 'inspected' 
        #2. do the same thing with the least 'expensive'node (part of an algorithm)
        done.append(the_least)  
        the_least = least_cost()

    if not the_least: return 'The path is unreachable!'
    costs[finish][1].append(finish)
    return costs[finish]

try:
    time, path = find_fastest(paths, 'S', 'F')
    print(f'The fastest path will take up {time} whatever. ')
    print(f'The fastest path is {path}. ')
except PathFindingMistake as patherr: 
    print(patherr)