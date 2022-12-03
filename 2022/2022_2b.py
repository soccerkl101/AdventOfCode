#!/usr/local/bin/python3
"""
--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
"""
import os, sys


with open(os.path.join(sys.path[0], "2022-2b-input.txt"), "r") as f:
    d=[]
    for i in f:
        d.append(i.strip())

sum=0
for i in d:
    THEM, ME = i.split(" ")
    if THEM=="A":
        #A is rock
        #X is Loss, Y is draw, Z is win
        if ME=="X":
            sum+=3
        if ME=="Y":
            sum+=1
            sum+=3
        if ME=="Z":
            sum+=2
            sum+=6
    if THEM=="B":
        #B is paper
        if ME=="X":
            sum+=1
        if ME=="Y":
            sum+=2
            sum+=3
        if ME=="Z":
            sum+=3
            sum+=6
    if THEM=="C":
        #C is scissor
        if ME=="X":
            sum+=2
        if ME=="Y":
            sum+=3
            sum+=3
        if ME=="Z":
            sum+=1
            sum+=6
print(sum)
