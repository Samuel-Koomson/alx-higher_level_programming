#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
#if tuples have less than 2 elements, add zeros to them
    x = tuple_a + (0, 0)[:len(tuple_a)-2]
    y = tuple_b + (0, 0)[:len(tuple_b)-2]
    
#return the sum of the two tuples matching the indices of the first two elements in each tuple
    return(x[0] + y[0], x[1] + y[1])
