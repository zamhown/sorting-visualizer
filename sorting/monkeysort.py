# Script Name     : monkeysort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Monkey sorting algorithm which can do nothing but be funny.

import copy
import random
from .data import Data

def monkey_sort(data_set, frame_count):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    dataes = [data.value for data in data_set]
    flag = False
    while not flag:
        flag = True
        for i in range(Data.data_count - 1):
            # FRAME OPERATION BEGIN
            ds = [Data(d) for d in dataes]
            frames.append(ds)
            ds[i].set_color('r')
            ds[i+1].set_color('k')
            if len(frames) == frame_count:
                return frames
            # FRAME OPERATION END
            if dataes[i] > dataes[i+1]:
                flag = False
                break
        if not flag:
            random.shuffle(dataes)
    # FRAME OPERATION BEGIN
    frames.append(Data(d) for d in dataes)
    return frames
    # FRAME OPERATION END