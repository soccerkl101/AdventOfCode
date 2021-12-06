"""
--- Part Two ---
Suppose the lanternfish live forever and have unlimited food and space. Would they take over the entire ocean?

After 256 days in the example above, there would be a total of 26984457539 lanternfish!

How many lanternfish would there be after 256 days?
"""

f = open("C:\\Users\socce\github\AdventOfCode\\2021\\2021_6b-input.txt", "r")

d=[]
for i in f:
    d.append(i.strip())

d = list(map(int, d[0].split(',')))
initial=len(d)
print(initial)
print(d)

counts={}
for i in range(9):
    if i not in counts:
        counts[i]=0
print(counts)

for i in d:
    counts[i]+=1
print(counts)

for days in range(256):
    zero=counts[0]
    counts[0]=counts[1]
    counts[1]=counts[2]
    counts[2]=counts[3]
    counts[3]=counts[4]
    counts[4]=counts[5]
    counts[5]=counts[6]
    counts[6]=counts[7]
    counts[7]=counts[8]
    counts[8]=zero
    counts[6]+=zero
    initial +=zero
print(initial)
