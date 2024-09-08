'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using list of sets

    graph = [
        {'b', 'e'},  # a points to b and e.
        {'c'},       # b points to c.
        {'d', 'e'},  # c points to d and e.
        {'b'},       # d points back to b.
        set()        # e has no outgoing connections.
    ]
    
    return graph

def part_2_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using list of dicts

    graph = [
        ['b', 'e', 'a'],  # a points to b, e, and itself (a)
        ['c'],            # b points to c
        ['a', 'e', 'd'],  # c points to a, e, and d
        [],               # d doesn't point anywhere
        ['d']             # e points to d
    ]
    
    return graph
def part_3_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using list of dicts.

    graph = [
        {'b': 1, 'e': 4, 'a': 8 },  # a points to b (weight 1) and e (weight 4)
        {'c': 3},                   # b points to c (weight 3)
        {'e': 4, 'a': 2},           # c points to d (weight 4) and e (weight 4)
        {},                         # d doesnt exist
        {}                          # e has no outgoing connections
    ]
    
    return graph


def part_4_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using dicts of sets.

    graph = {
        'a': {'b', 'e', 'a'},   # a points to b, e and a itself 
        'b': {'c'},             # b points to c
        'c': {'a'},             # c points to a
        'e': {},                # e has no outgoing connections
        'd': set()              # d doesnt exist
    }
    
    return graph

def part_5_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using dicts of dicts.

    graph = {
        'a': {'b': 5},              # a points to b (weight 5)
        'b': {'e': 3},              # b points to e (weight 3) 
        'e': {'b': 2, 'a': 6},      # e points to b (weight 2) and a (weight 6)
        'c': {},                    # c has no outgoing connections
        'd': {}                     # d has no outgoing connections
    }
    
    return graph