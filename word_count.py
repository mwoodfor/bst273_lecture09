#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

print(args.data_file)

fh = open(args.data_file)

#initalize the count variables
lines = 0
words = 0
chars = 0

for line in fh:
	lines += 1
print(lines)
#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
