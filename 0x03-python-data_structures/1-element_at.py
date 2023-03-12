#!/usr/bin/python3
"""Function that retrieves elements from a list"""
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return None
    for idx in my_list:
        if idx > my_list:
            return None
    
