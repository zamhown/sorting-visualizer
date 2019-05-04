# Script Name     : output.py
# Author          : Howard Zhang
# Created         : 14th June 2018
# Last Modified	  : 4th May 2019
# Version         : 1.2
# Modifications	  : 1.2 - Added the new option of modifying the number of items to be sorted.
# Description     : Processing user's input, Playing animations and generating animation files.

import random
import os
import sys
import re
from matplotlib import pyplot as plt
from matplotlib import animation
from sorting.data import Data
from sorting.selectionsort import selection_sort
from sorting.bubblesort import bubble_sort
from sorting.insertionsort import insertion_sort
from sorting.shellsort import shell_sort
from sorting.mergesort import merge_sort
from sorting.quicksort import quick_sort
from sorting.heapsort import heap_sort
from sorting.combsort import comb_sort
from sorting.monkeysort import monkey_sort

stype_dic = {'all': -1,
             'insertion-sort': 0, 'shell-sort':1,  'selection-sort': 2, 
             'merge-sort': 3,     'quick-sort': 4, 'heap-sort': 5,
             'bubble-sort': 6,    'comb-sort': 7}
titles = [r'Insertion Sort ($O(n^2)$)',          r'Shell Sort ($O(n \cdot log_2(n)^2)$)', r'Selection Sort ($O(n^2)$)',
          r'Merge Sort ($O(n \cdot log_2(n))$)', r'Quick Sort ($O(n \cdot log_2(n))$)',   r'Heap Sort ($O(n \cdot log_2(n))$)',
          r'Bubble Sort ($O(n^2)$)',             r'Comb Sort ($O(n \cdot log_2(n))$)',    r'Monkey Sort ($O(n!)$)',]
funs = [insertion_sort, shell_sort, selection_sort,
        merge_sort,     quick_sort, heap_sort,
        bubble_sort,    comb_sort,  monkey_sort]

def create_original_data(dtype):
    data = []
    if dtype == 'random':
        data = list(range(1, Data.data_count + 1))
        random.shuffle(data)
    elif dtype == 'reversed':
        data = list(range(Data.data_count, 0, -1))
    elif dtype == 'few-unique':
        d = Data.data_count // 4
        for i in range(0, d):
            data.append(d)
        for i in range(d, d*2):
            data.append(d*2)
        for i in range(d*2, d*3):
            data.append(d*3)
        for i in range(d*3, Data.data_count):
            data.append(Data.data_count)
        random.shuffle(data)
    elif dtype == 'almost-sorted':
        data = list(range(1, Data.data_count + 1))
        a = random.randint(0, Data.data_count - 1)
        b = random.randint(0, Data.data_count - 1)
        while a == b:
            b = random.randint(0, Data.data_count - 1)
        data[a], data[b] = data[b], data[a]
    return data

def draw_chart(stype, original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    axs = fig.add_subplot(111)
    axs.set_xticks([])
    axs.set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)
    
    # Get the data of all frames.
    frames = funs[stype](data_set)
    # Output the frame count.
    print('%s: %d frames.' % (re.findall(r'\w+ Sort', titles[stype])[0], len(frames)))

    # Animation function. This is called sequentially.
    # Note: fi is framenumber.
    def animate(fi):
        bars = []
        if(len(frames) > fi):
            axs.cla()
            axs.set_title(titles[stype])
            axs.set_xticks([])
            axs.set_yticks([])
            bars += axs.bar(list(range(Data.data_count)),        # X
                            [d.value for d in frames[fi]],       # data
                            1,                                   # width
                            color=[d.color for d in frames[fi]]  # color
                            ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=len(frames), interval=frame_interval)
    return plt, anim

def draw_all_charts(original_data, frame_interval):
    # First set up the figure, the axis, and the plot elements we want to animate.
    axs = []
    frames = []
    fig = plt.figure(1, figsize=(16, 9))
    data_set = [Data(d) for d in original_data]
    for i in range(9):
        axs.append(fig.add_subplot(331 + i))
        axs[-1].set_xticks([])
        axs[-1].set_yticks([])
    plt.subplots_adjust(left=0.01, bottom=0.02, right=0.99, top=0.95,
                        wspace=0.05, hspace=0.15)

    # Get the data of all frames.
    for i in range(8):
        frames.append(funs[i](data_set))
    # The frame count of monkey sort is 50 more than the maximum one.
    frames.append(funs[8](data_set, max(len(f) for f in frames) + 50))

    # Output the frame counts of all chart.
    names = []
    max_name_length = 0
    frame_counts = []
    max_frame_length = 0
    for i in range(9):
        names.append(re.findall(r'\w+ Sort', titles[i])[0] + ':')
        if len(names[-1]) > max_name_length:
            max_name_length = len(names[-1])
        frame_counts.append(len(frames[i]))
        if len(str(frame_counts[-1])) > max_frame_length:
            max_frame_length = len(str(frame_counts[-1]))
    for i in range(9):
        print('%-*s %*d frames' % (max_name_length, names[i], max_frame_length, frame_counts[i]))

    # Animation function. This is called sequentially.
    # Note: fi is framenumber.
    def animate(fi):
        bars = []
        for i in range(9):
            if(len(frames[i]) > fi):
                axs[i].cla()
                axs[i].set_title(titles[i])
                axs[i].set_xticks([])
                axs[i].set_yticks([])
                bars += axs[i].bar(list(range(Data.data_count)),           # X
                                   [d.value for d in frames[i][fi]],       # data
                                   1,                                      # width
                                   color=[d.color for d in frames[i][fi]]  # color
                                   ).get_children()
        return bars

    # Call the animator.
    anim = animation.FuncAnimation(fig, animate, frames=max(len(f) for f in frames), interval=frame_interval)
    return plt, anim

if __name__ == "__main__":
    try:
        Data.data_count = int(input('Please set the number of items to be sorted(32): '))
    except:
        Data.data_count = 32
    if len(sys.argv) > 1:
        # Type of sort algorithm.
        stype = -1
        if len(sys.argv) > 2:
            if sys.argv[2] in stype_dic:
                stype = stype_dic[sys.argv[2]]
            else:
                print('Error: Wrong argument!')
                exit()
        stype_str = list(stype_dic.keys())[list(stype_dic.values()).index(stype)]

        # Type of original data.
        dtype = 'random'
        if len(sys.argv) > 3:
            dtype = sys.argv[3]
            if dtype not in ('random', 'reversed', 'few-unique', 'almost-sorted'):
                print('Error: Wrong argument!')
                exit()
        od = create_original_data(dtype)

        if sys.argv[1] == 'play':
            try:
                fi = int(input('Please set the frame interval(100): '))
            except:
                fi = 100
            plt, _ = draw_all_charts(od, fi) if stype == -1 else draw_chart(stype, od, fi)
            plt.show()
        elif sys.argv[1] == 'save-mp4':
            default_fn = stype_str + '-' + dtype + '-animation'
            fn = input('Please input a filename(%s): ' % default_fn)
            if fn == '':
                fn = default_fn
            try:
                fps = int(input('Please set the fps(25): '))
            except:
                fps = 25
            _, anim = draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            print('Please wait...')
            anim.save(fn + '.mp4', writer=animation.FFMpegWriter(fps=fps, extra_args=['-vcodec', 'libx264']))
            print('The file has been successfully saved in %s' % os.path.abspath(fn + '.mp4'))
        elif sys.argv[1] == 'save-html':
            default_fn = stype_str + '-' + dtype + '-animation'
            fn = input('Please input a filename(%s): ' % default_fn)
            if fn == '':
                fn = default_fn
            try:
                fps = int(input('Please set the fps(25): '))
            except:
                fps = 25
            _, anim = draw_all_charts(od, 100) if stype == -1 else draw_chart(stype, od, 100)
            print('Please wait...')
            anim.save(fn + '.html', writer=animation.HTMLWriter(fps=fps))
            print('The file has been successfully saved in %s' % os.path.abspath(fn + '.html'))