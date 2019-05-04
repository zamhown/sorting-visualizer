# Script Name     : mergesort.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 14th June 2018
# Version         : 1.0
# Modifications	  : 
# Description     : Merge sorting algorithm.

import copy
from .data import Data

def merge_sort(data_set):
    # FRAME OPERATION BEGIN
    frames = [data_set]
    # FRAME OPERATION END
    ds = copy.deepcopy(data_set)
    split_merge(ds, 0, Data.data_count, frames)
    # FRAME OPERATION BEGIN
    frames.append(ds)
    return frames
    # FRAME OPERATION END

def split_merge(ds, head, tail, frames):
    mid = (head + tail) // 2
    # Split.
    if tail - head > 2:
        split_merge(ds, head, mid, frames)
        split_merge(ds, mid, tail, frames)
    # FRAME OPERATION BEGIN
    ds_yb = copy.deepcopy(ds)
    for i in range(head, mid):
        ds_yb[i].set_color('y')
    for i in range(mid, tail):
        ds_yb[i].set_color('b')
    # FRAME OPERATION END
    # Merge.
    left = head
    right = mid
    tmp_list = []
    for i in range(head, tail):
        # FRAME OPERATION BEGIN
        frames.append(copy.deepcopy(ds_yb))
        # FRAME OPERATION END
        if right == tail or (left < mid and ds[left].value <= ds[right].value):
            tmp_list.append(ds[left])
            # FRAME OPERATION BEGIN
            frames[-1][left].set_color('r')
            # FRAME OPERATION END
            left += 1
        else:
            tmp_list.append(ds[right])
            # FRAME OPERATION BEGIN
            frames[-1][right].set_color('r')
            # FRAME OPERATION END
            right += 1
    for i in range(head, tail):
        ds[i] = tmp_list[i-head]
    # FRAME OPERATION BEGIN
    frames.append(copy.deepcopy(ds))
    # FRAME OPERATION END

