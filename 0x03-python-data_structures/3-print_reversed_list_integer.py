#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        my_list.reverse()
        for rev in range(len(my_list)):
            print(f("{:d} {(my_list[rev])}"))
