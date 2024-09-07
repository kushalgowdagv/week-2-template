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
    pass

def part_4_graph():
    pass

def part_5_graph():
    pass
