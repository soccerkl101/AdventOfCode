#!/usr/local/bin/python3
"""
--- Part Two ---
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
"""
import os, sys


with open(os.path.join(sys.path[0], "2022-1a-input.txt"), "r") as f:
    d=[]
    for i in f:
        d.append(i.strip())

first=0
second=0
third=0
curr=0

for i in d:
    if i!="":
        curr+=int(i)
    else:
        if curr > first:
            third=second
            second=first
            first = curr
            curr = 0
        elif curr > second:
            third=second
            second=curr
            curr=0
        elif curr > third:
            third=curr
            curr=0
        curr = 0

print(first+second+third)


    