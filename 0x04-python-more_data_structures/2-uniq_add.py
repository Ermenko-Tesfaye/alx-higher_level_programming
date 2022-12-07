#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp_list = []
    total = 0
    for i in my_list:
        if i in tmp_list:
            continue
        else:
            tmp_list.append(i)
            total += i
    return total
