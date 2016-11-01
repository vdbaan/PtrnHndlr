#!/usr/bin/env python
from __future__ import print_function
import argparse
import string

pattern = ""
for c1 in list(string.lowercase):
    for c2 in list(string.uppercase):
        for c3 in list(string.lowercase):
            for c4 in range(0,10):
                pattern = pattern + "%s%s%s%d"%(c1,c2,c3,c4)

def create(size=10):
    '''aAa0aAa1aAa2 ... etc'''
    print(pattern[0:int(size)])


def locate(ptrn):
    print( pattern.index(ptrn))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ALike the Metasploit pattern_create and pattern_locate')
    parser.add_argument('-c','--create', metavar="SIZE")
    parser.add_argument('-l','--locate', metavar="PATTERN")
    args = parser.parse_args()
    if args.create == None and args.locate == None:
        parser.print_help()
        exit(0)
    if args.create:
        create(args.create)
    elif args.locate:
        locate(args.locate)