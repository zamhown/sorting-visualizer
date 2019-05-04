# Script Name     : bubblesort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 15th June 2018
# Version         : 1.1
# Modifications	  : 1.1 - Added the variable flag to optimize the algorithm.
# Description     : Bubble sorting algorithm.

import copy
from .data import Data

def bubble_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    for i in range(Data.data_count-1):
        flag = False
        for j in range(Data.data_count-i-1):
            if ds[j].value > ds[j+1].value:
                ds[j], ds[j+1] =  ds[j+1], ds[j]
                flag = True
            # FRAME OPERATION BEGIN
            frames.append(copy.deepcopy(ds))
            frames[-1][j+1].set_color('r')
            # FRAME OPERATION END
        if not flag:
            break
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END
