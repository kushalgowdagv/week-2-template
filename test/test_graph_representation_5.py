import subprocess
import re
from student_code import part_2_graph 

node_dict={'a':0,'b':1,'c':2,'d':3,'e':4}

# Test 3: Check for unhandled pylint style recommendations
def test_part_2():
       graph=part_2_graph()
       assert type(graph)==list
       assert 'b' in graph[node_dict['a']]
       assert type(graph[node_dict['a']])==list