#!/usr/local/bin/python3
"""
--- Part Two ---
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""
import os, sys


with open(os.path.join(sys.path[0], "2022-4b-input.txt"), "r") as f:
    d=[]
    for i in f:
        d.append(i.strip())

sum=0

for i in d:
    elfONE, elfTWO = i.split(',')
    elfONE_one, elfONE_two = elfONE.split('-')
    elfTWO_one, elfTWO_two = elfTWO.split('-')
    if (int(elfTWO_one) >= int(elfONE_one)) and (int(elfTWO_one) <= int(elfONE_two)):
        sum+=1
        continue
    if int(elfONE_one) >= int(elfTWO_one) and int(elfONE_one) <= int(elfTWO_two):
            sum+=1
print(sum)