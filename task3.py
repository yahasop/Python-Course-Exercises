#!/usr/bin/env python3

#This script only works with the access.log.5 file within this repo
#Provides a list of servers that requested access and how many times they tried
#Many attempts could be a sign of malicious intentions

import argparse
import collections

parser = argparse.ArgumentParser(description='Program to receive a log filet')

parser.add_argument('filename', help='Pass a single filename') #Single argument

args = parser.parse_args()

#The file's lines are read one by one. Then they are splitted by the '- -' sign, only at the first encounter of the sign (gets two string for each line). 
#Then it retrieves the first value (index 0) and append those into a new list ip_list
count = {} #Dictionary initialization
ip_list = [] #List initialization
with open(args.filename) as f:
    for line in f:
        first_val = line.split('- -', 1)[0] 
        ip_list.append(first_val.strip())

#Using a collections method, easily counts ocurrences of each value on the list ip_list, passing the value and its ocurrence into a dictionary counter
counter = dict(collections.Counter(ip_list))

#Using the dictionary we can fetch the values and ocurrences with a for loop iterating over .items() function which returns key and values of the dict
for ip, ocurrence in counter.items():
    if ocurrence < 10:
        print(f"{ocurrence} connection requests for the IP: {ip}")
    else:
        print(f"{ocurrence} connection requests for the IP: {ip} [WARNING!!!]")
