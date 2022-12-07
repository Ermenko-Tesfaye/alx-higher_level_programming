#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_st = []
    for i in set_1:
        if i in set_2:
            common_st.append(i)
    return common_st
