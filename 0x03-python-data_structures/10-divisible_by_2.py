#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        listdivi = []
        for a in my_list:
            if a % 2 == 0:
                listdivi.append(True)
            else:
                listdivi.append(False)
        return(listdivi)
