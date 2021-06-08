'''
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
'''


f = open("C:\\Users\Kevin\github\AdventofCode_new\\2015_3.txt", "r")
data=[]
data2=[]
z=1
for i in f.read():
    if z%2==0:
        data.append(i)
        z+=1
    else:
        data2.append(i)
        z+=1


x=0
y=0
my_dict={(0,0):1}

for i in data:
    if i=="^":
        y+=1
    elif i=="v":
        y-=1
    elif i==">":
        x+=1
    else:
        x-=1

    my_dict[x,y]= my_dict.get((x,y), 0) +1

x=0
y=0

for i in data2:
    if i=="^":
        y+=1
    elif i=="v":
        y-=1
    elif i==">":
        x+=1
    else:
        x-=1

    my_dict[x,y]= my_dict.get((x,y), 0) +1

print(len(my_dict))
