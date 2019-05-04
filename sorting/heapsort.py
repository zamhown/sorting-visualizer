# Script Name     : heapsort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Heap sorting algorithm.

import copy
from .data import Data

def heap_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    # Build a max heap and adjust from the last parent node.
    for i in range(Data.data_count//2-1, -1, -1):
        heap_adjust(ds, i, Data.data_count, frames)
    for i in range(Data.data_count-1, 0, -1):
        # Put the maximum in the position of i.
        ds[i], ds[0] = ds[0], ds[i]
        # Adjust the heap from 0 to i-1.
        heap_adjust(ds, 0, i, frames)
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END

def heap_adjust(ds, head, tail, frames):
    # The left child of head.
    i = head * 2 + 1
    while i < tail:
        # Choose a bigger child
        if i + 1 < tail and ds[i].value < ds[i+1].value:
            i += 1
        # FRAME OPERATION BEGIN
        ds_c = color(ds, tail)
        frames.append(ds_c)
        ds_c[i].set_color('k')
        ds_c[head].set_color('r')
        # FRAME OPERATION END
        # If two children are both less than parent, do nothing.
        if ds[i].value <= ds[head].value:
            break
        ds[head], ds[i] = ds[i], ds[head]
        # FRAME OPERATION BEGIN
        ds_c = copy.deepcopy(ds_c)
        frames.append(ds_c)
        ds_c[head], ds_c[i] = ds_c[i], ds_c[head]
        # FRAME OPERATION END
        head = i
        i = i * 2 + 1

def color(ds, n):
    # FRAME OPERATION BEGIN
    ds_c = copy.deepcopy(ds)
    head = 0
    tail = 1
    count = 1
    depth = 0
    colors = 'bmgcy'
    while head < n:
        for i in range(head, min(tail, n)):
            ds_c[i].set_color(colors[depth % len(colors)])
        head = tail
        count *= 2
        tail += count
        depth += 1
    return ds_c
    # FRAME OPERATION END
    

