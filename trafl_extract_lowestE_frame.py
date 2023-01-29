#!/usr/bin/env python

import sys
import os

if(len(sys.argv) < 2):
    print ("usage: trafl_finds_lowestE_frame.py file.trafl", file=sys.stderr)
    sys.exit(1)

inpfilename = sys.argv[1]

if(inpfilename[-6:]!=".trafl"):
    print ("extension of input file: "+inpfilename+" has to be .trafl", file=sys.stderr)
    sys.exit(1)

if(os.path.exists(inpfilename) is False):
    print ("specified file: "+inpfilename+" doesn't exist", file=sys.stderr)
    sys.exit(1)

counter = 1
lowest_frame = 1
lowest_energy = 1000000.0

inpfile = open(inpfilename)

curr_line = inpfile.readline()
while(curr_line):

    if(len(curr_line) < 100):
        splitted_line = curr_line.split()
        curr_energy = float(splitted_line[-2])

        if(lowest_energy > curr_energy):
            lowest_energy = curr_energy
            lowest_frame = counter
            lowestE_header = curr_line
            lowestE_coords = inpfile.readline()

        counter += 1
    curr_line = inpfile.readline()

inpfile.close()

print(lowest_frame, lowest_energy)

outfilename = inpfilename.replace(".trafl","_minE.trafl")
print(outfilename)

original_stdout = sys.stdout
with open(outfilename, 'w') as f:
    sys.stdout = f
    print (lowestE_header)
    print (lowestE_coords)
    sys.stdout = original_stdout
