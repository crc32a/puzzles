#!/usr/bin/env python

import sys
import os

def printf(format,*args): sys.stdout.write(format%args)

#count flips 0 means forward 1 means back
def get_cheaper_flip(p):
    commands = [[],[]]
    n = len(p)
    # Start by trying forward flips first
    flipping = False
    start_flip = 0

    #Start the case for flipping 1s to 0
    for i in range(0,n):
        if flipping and p[i] == 0:
            commands[0].append((start_flip, i - 1))
            flipping = False
            continue #Your at the end of a flip session

        if flipping and p[i] == 1:
            continue #Were still in flipping 1 to 0

        if not flipping and p[i] == 0:
            continue #nothing to do were in a 0 run

        if not flipping and p[i] == 1:
            flipping = True
            start_flip = i
            #This is the start of a flip run
            continue
    if flipping:
        commands[0].append((start_flip, n-1))
        #Don't for get to flip the last hat if we were flipping and mark
        #it as a command
    start_flip = 0
    flippng = False

    #Consider the case of flipping 0s to 1
    for i in range(0,n):
        if flipping and p[i] == 0:
            continue
            #Were in the middle of a flip run

        if flipping and p[i] == 1:
            commands[1].append((start_flip, i - 1))
            flipping = False
            continue
            #This is the end of a flip run

        if not flipping and p[i] == 0:
            flipping = True
            start_flip = i
            continue
            #This is the start of a flip run

        if not flipping and p[i] == 1:
            continue
            #Nothing to do
    if flipping:
        commands[1].append((start_flip, n-1))
    return commands

if __name__ == "__main__":
    p = []
    v = []
    chmap = {"f": 0, "b": 1}
    rvmap = {"f": 0, "b": "1"}

    for ch in sys.argv[1]:
        if ch in chmap:
            p.append(chmap[ch])
            v.append(ch)

    printf("Solving for %s\n", v)
    solutions = get_cheaper_flip(p)
    printf("forward = %s\n", solutions[0])
    printf("backword = %s\n", solutions[1])
    printf("forward_count = %d\n",  len(solutions[0]))
    printf("backword_count = %d\n", len(solutions[1]))
