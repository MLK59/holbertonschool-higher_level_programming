#!/usr/bin/python3
# This function returns a list with all values multiplied by a number without using any loops
def mutiply_list_map(my_list=[], number=0):
    return list(map((lambda x: x * number), my_list))
