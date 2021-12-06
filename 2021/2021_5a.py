"""
--- Day 5: Hydrothermal Venture ---
You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""
f = open("C:\\Users\socce\github\AdventOfCode\\2021\\2021_5a-input.txt")

d=[]
for i in f:
    i=i.strip().split('->')
    d.append((list(map(int,(i[0].split(",")))),list(map(int,(i[1].split(","))))))
    #https://www.geeksforgeeks.org/python-map-function/ "Code 4's example"


board={}
count=0
for i in d:
    if i[0][0] == i[1][0] or i[0][1] == i[1][1]:
        maxX = max(i[0][0], i[1][0])
        maxY = max(i[0][1], i[1][1])
        minX = min(i[0][0], i[1][0])
        minY = min(i[0][1], i[1][1])

        for x in range(minX, maxX+1):
            for y in range(minY, maxY+1):
                board[(x,y)] = board.get((x,y),0) + 1
                #https://stackoverflow.com/questions/3496518/using-a-dictionary-to-count-the-items-in-a-list
print(board)
print(board.values())
for i in board.values():
    if i > 1:
        count+=1
print(count)
