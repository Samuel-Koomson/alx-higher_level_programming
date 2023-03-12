#!/usr/bin/python3
"""Function that retrieves elements from a list"""
def element_at(my_list, idx):
    for x in my_list:
        if idx < 0 or idx >= len(my_list):
            return None
   	return my_list[idx]
    
