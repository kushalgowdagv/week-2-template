'''Representing graphs'''

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

def part_1_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using list of sets

    graph = [
        {'b', 'e'},  # a points to b and e
        {'a', 'c'},  # b points to c and also back to a.
        {'d', 'e'},  # c points to d and e.
        {'b'},       # d points back to b.
        set()        # e has no outgoing connections.
    ]
    
    return graph

def part_2_graph():

    # Each index in the list corresponds to the node, and the set contains the nodes it points to using list of lists

    graph = [
        ['b', 'e', 'a'],  # a points to b, e, and itself (a)
        ['c'],            # b points to c
        ['a', 'e', 'd'],  # c points to a, e, and d
        [],               # d doesn't point anywhere
        ['d']             # e points to d
    ]
    
    return graph
def part_3_graph():
    graph = [
        {'b': 1, 'e': 4, 'a': 8 },  # a points to b (weight 1) and e (weight 4)
        {'c': 3},          # b points to c (weight 3)
        {'d': 4, 'e': 4, 'a': 4},  # c points to d (weight 4) and e (weight 4)
        {'b': 2},          # d points to b (weight 2)
        {}                 # e has no outgoing connections
    ]
    
    return graph


def part_4_graph():
    graph = {
        'a': {'b', 'e', 'a'},  # a points to b, e and a itself 
        'b': {'c'},  # b points to c
        'c': {'a'},       # c points to a
        'e': {},  # e points to b and c
        'd': set()        # d has no outgoing connections
    }
    
    return graph

def part_5_graph():
    pass
