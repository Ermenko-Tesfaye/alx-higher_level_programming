#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_l = []
    for i in my_list:
        copy_l.append(i)
    if idx < 0 or idx >= len(my_list):
        return copy_l
    copy_l[idx] = element
    return copy_l
