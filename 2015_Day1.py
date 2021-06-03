f = open("C:\\Users\Kevin\Desktop\Adventofcodestuff\\2015_1.txt", "r")

#print(f.read())

floor=0
position=0

for i in f.read():
    print(i)
    if i == "(":
        floor+=1
        position+=1
    elif i == ")":
        floor-=1
        position+=1
        if floor < 0:
            break
    print(floor)
print(floor)
print(position)
