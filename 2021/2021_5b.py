"""
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""

f = open("C:\\Users\socce\github\AdventOfCode\\2021\\2021_5b-input.txt")

d=[]
for i in f:
    i=i.strip().split('->')
    d.append((list(map(int,(i[0].split(",")))),list(map(int,(i[1].split(","))))))
    #https://www.geeksforgeeks.org/python-map-function/ "Code 4's example"

board={}
count=0
for i in d:
    maxX = max(i[0][0], i[1][0])
    maxY = max(i[0][1], i[1][1])
    minX = min(i[0][0], i[1][0])
    minY = min(i[0][1], i[1][1])
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]:

        for x in range(minX, maxX+1):
            for y in range(minY, maxY+1):
                board[(x,y)] = board.get((x,y),0) + 1
                #https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
    elif (i[0][0] < i[1][0] and i[0][1] < i[1][1]) or (i[0][0] > i[1][0] and i[0][1] > i[1][1]):
        for x in range(maxX - minX+1):
            board[(minX+x,minY+x)]=board.get((minX+x,minY+x),0) + 1
    else:
        for x in range(maxX - minX+1):
            board[(minX+x,maxY-x)]=board.get((minX+x,maxY-x),0) + 1
for i in board.values():
    if i > 1:
        count+=1
print(count)
