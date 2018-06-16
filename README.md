# Sorting Visualizer
Some python scripts which can visualize several famous sorting algorithms and generate the animations via Matplotlib.  
![example](https://raw.githubusercontent.com/zamhown/sorting-visualizer/master/img/example.png)
## Environment Configuring
* Install Python or Anaconda which includes it.
* Install [Matplotlib](https://matplotlib.org/users/installing.html) via pip. However, if you have installed Anaconda before, you needn't install Matplotlib any more.
* If you need export the animations of sorting algorithms as MP4 files, you should download an offical release of FFMpeg (there is [the link](https://ffmpeg.zeranoe.com/builds/)). Taking Windows for example, after downloading, extract it to anywhere, and add `[your_path]/ffmpeg/bin` to the environment variable `PATH` to ensure you can run the command `ffmpeg` directly in CMD.
## Instructions
Access the project's root directory using CMD or Shell, run the command like the following format to call all functions:  
`python output.py arg1 [arg2 [arg3]]`  

The following are the details of the three arguments:  
* There are three posible arguments as "*arg1*":
    * `play` : Play an animation of a specific sorting algorithm or all algorithms in a new window, as a "figure" to Matplotlib.
    * `save-html` : Save the animation as a HTML page with a sequence of images.
    * `save-mp4` : Save the animation as a MP4 video.
* There are nine posible arguments as "*arg2*":
    * `all` (default) : Show the visualization of all sorting algorithms in the animation.
    * `bubble-sort` : Only show the visualization of bubble sorting algorithm in the animation. The following arguments have similar functions.
    * `comb-sort`
    * `heap-sort`
    * `insertion-sort`
    * `merge-sort`
    * `quick-sort`
    * `selection-sort`
    * `shell-sort`
* There are four posible arguments as "*arg3*":
    * `almost-sorted` : Sort an almost-sorted sequence.
    * `few-unique` : Sort a few-unique sequence.
    * `random` (default) : Sort a random sequence.
    * `reversed` : Sort a descending sequence.
For example, run `python output.py play heap-sort reversed` to create a new window to play the animation of sorting, which use heap sorting algorithms and sort a descending sequence.

