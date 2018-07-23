#!/usr/bin/python

import sys
import os

def printf(format,*args): sys.stdout.write(format%args)

#count flips 0 means forward 1 means back
if __name__ == "__main__":
    sched = []
    n = len(sys.argv)
    i = 1
    #Get celbrities
    while i + 1 < n:
        celeb = (int(sys.argv[i]),int(sys.argv[i+1]))
        sched.append(celeb)
        i += 2
sched.sort()
printf("schedule = %s\n", sched)
printf("Counting each celeb at each hour\n")
min_h = sched[0][0]  # When first celeb arrives
max_h = sched[-1][1] # When last celeb leaves

celebs_at_hour = {}
max_celebs = 0
best_hour = -1
for h in range(min_h, max_h):
    celebs_present = 0
    for celeb in sched:
        if h >= celeb[0] and h < celeb[1]:
            celebs_present += 1
    celebs_at_hour[h] = celebs_present
    if max_celebs < celebs_present:
        best_hour = h
        max_celebs = celebs_present

printf("Schedule is: ")
for k in sorted(celebs_at_hour.keys()):
    printf("(%i, %i) ", k, celebs_at_hour[k])
printf("\n")
printf("Best hour is %i\n", best_hour)
