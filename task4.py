#!/usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser(description='Program to receive a string and find the ocurrences of single characters within it')

parser.add_argument('string', type=str, help='Pass a single string to store and process it')

args = parser.parse_args()

#Using a collections method function we can easily retrieve ocurrences in the string
count = dict(collections.Counter(args.string))

formatted_dict = [] #List initialization

#Iteration over the count dictionary items to append them to a list for easier manipulation in the output format
for letter, ocurrence in count.items():
    formatted_dict.append(f"{letter}:{ocurrence}") #Format output, generates a list with key and values in that format

#The join function simply joins all values of the formatted_dict list with a comma and space in between
print(f'Character ocurrences on the string "{args.string}" -----> {", ".join(formatted_dict)}')
