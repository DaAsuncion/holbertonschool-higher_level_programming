#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        return replace_in_list(my_list, idx, new_element)
