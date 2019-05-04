# Script Name     : quicksort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Quick sorting algorithm.

import copy
from .data import Data

def quick_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    qsort(ds, 0, Data.data_count, frames)
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END

def qsort(ds, head, tail, frames):
    if tail - head > 1:
        # FRAME OPERATION BEGIN
        ds_y = copy.deepcopy(ds)
        for i in range(head, tail):
            ds_y[i].set_color('y')
        # FRAME OPERATION END
        i = head
        j = tail - 1
        pivot = ds[j].value
        while i < j:
            # FRAME OPERATION BEGIN
            frames.append(copy.deepcopy(ds_y))
            frames[-1][i if ds[i].value == pivot else j].set_color('r')
            frames[-1][j if ds[i].value == pivot else i].set_color('k')
            # FRAME OPERATION END
            if ds[i].value > pivot or ds[j].value < pivot:
                ds[i], ds[j] = ds[j], ds[i]
                # FRAME OPERATION BEGIN
                ds_y[i], ds_y[j] = ds_y[j], ds_y[i]
                frames.append(copy.deepcopy(ds_y))
                frames[-1][i if ds[i].value == pivot else j].set_color('r')
                frames[-1][j if ds[i].value == pivot else i].set_color('k')
                # FRAME OPERATION END
            if ds[i].value == pivot:
                j -= 1
            else:
                i += 1
        qsort(ds, head, i, frames)
        qsort(ds, i+1, tail, frames)

