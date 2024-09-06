#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='Program to check a filename extension') #Parser initialization

parser.add_argument('filename', help='Pass a filename to check its extension') #Adds the one argument the program receives

args = parser.parse_args() #Store the argument in a variable

#Using a try and except bloc this tries to check if the file provided has an extension
try:
    if "." in args.filename: #A file's extension is after the dot, so it checks is file name has a dot in it
        extension = args.filename.split(".",1)[1] #This spli method, splits by a dot, one separation, and then retrieves the second positio
        print(f"The file has an extension. Is a '.{extension}' file")
    else:
        raise IndexError("File does not have an extension") #IndexError is the most common error when providing the filename
except:
    print(f"The file does not have an extension. Original filename is '{args.filename}'")
