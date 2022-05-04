#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newreplace = my_list.copy()
    for n, i in enumerate(newreplace):
        if i == search:
            newreplace[n] = replace
            return newreplace
