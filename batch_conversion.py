import os, sys

def time2sec(time_str):
    # time_str in the format of mm:ss
    time_components = time_str.split(':')
    return int(time_components[0])*60 + int(time_components[1])

inout_file = open(sys.argv[1], 'r')

for line in inout_file:
    items = line.split()
    source_vid = items[0]
    target_vid = items[1]
    in_time = time2sec(items[2]) # i.e. start time
    out_time = time2sec(items[3]) # i.e. end time
    duration = out_time - in_time
    os.system(' '.join(['vid2mp4_timed.sh', source_vid, target_vid, str(in_time), str(duration)]))
    
