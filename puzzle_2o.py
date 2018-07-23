#!/usr/bin/python

import sys
import os

def printf(format,*args): sys.stdout.write(format%args)

#count flips 0 means forward 1 means back
if __name__ == "__main__":
    sched = []
    celeb_hour_count = {}
    n = len(sys.argv)
    i = 1
    #Get celbrities
    while i + 1 < n:
        arrive = int(sys.argv[i])
        depart = int(sys.argv[i+1])
        sched.append( (arrive, 1)  ) #When one arrives add one
        sched.append( (depart, -1) ) #when one leaves subtract one
        i += 2

    sched.sort() # adds O(n log(n)) complexity
    celebs_now = 0
    min_h = sched[0][0]
    max_h = sched[-1][0]
    n = len(sched)
    max_celebs = 0
    max_celebs_hour = 0;
    printf("sched = %s\n", sched)
    for h in range(min_h,max_h+1):
        celeb_hour_count[h] = 0  #Initialize each out at zero
    for i in range(0,n):
        h = sched[i][0]
        celebs_now += sched[i][1]
        celeb_hour_count[h] = celebs_now

    printf("Celebs at hour = [ ")
    max_celebs = 0
    max_celebs_hour = 0
    for h in range(min_h, max_h):
        celebs = celeb_hour_count[h]
        if celebs > max_celebs:
            max_celebs = celebs
            max_celebs_hour = h
        printf("(%i , %i), ", h, celebs)
    printf("\n")
    printf("Best hour is %i\n", max_celebs_hour);

                
