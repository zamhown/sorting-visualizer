# Script Name     : selectionsort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Selection sorting algorithm.

import copy
from .data import Data

def selection_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(0, Data.data_count-1):
        for j in range(i+1, Data.data_count):
            # FRAME OPERATION BEGIN
            ds_r = copy.deepcopy(ds)
            frames.append(ds_r)
            ds_r[i].set_color('r')
            ds_r[j].set_color('k')
            # FRAME OPERATION END
            if ds[j].value < ds[i].value:
                ds[i], ds[j] = ds[j], ds[i]
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END