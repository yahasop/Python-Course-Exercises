#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Program to receive N number of arguments and process them')

#This argument receives only integers, and adds them to a list with nargs='+'
parser.add_argument('integer', metavar='N', nargs='+', type=int, help='Pass a list of integers to store and process them') 

args = parser.parse_args()

#Using built-in functions to remove duplicates (set), sorting elements and create a tuple from the list
non_duplicates = tuple(sorted(set(args.integer))) 

#This retrieves the max and min from the tuple
non_duplicates_min = min(non_duplicates)
non_duplicates_max = max(non_duplicates)

print(f"The non duplicates tuple is: {non_duplicates}")
print("")
print(f"The minimum is '{non_duplicates_min}' and maximum is '{non_duplicates_max}'")
