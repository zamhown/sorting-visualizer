# Script Name     : combsort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Comb sorting algorithm.

import copy
from .data import Data

def comb_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    # Division of two pointers.
    div = int(Data.data_count/1.3)
    while div >= 1:
        for i in range(Data.data_count - div):
            # FRAME OPERATION BEGIN
            frames.append(copy.deepcopy(ds))
            frames[-1][i].set_color('r')
            frames[-1][i+div].set_color('k')
            # FRAME OPERATION END
            if ds[i].value > ds[i+div].value:
                ds[i], ds[i+div] = ds[i+div], ds[i]
                # FRAME OPERATION BEGIN
                frames.append(copy.deepcopy(ds))
                frames[-1][i+div].set_color('r')
                frames[-1][i].set_color('k')
                # FRAME OPERATION END
        div = int(div/1.3)
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END