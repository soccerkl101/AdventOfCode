f = open("C:\\Users\Kevin\Desktop\Adventofcodestuff\\2015_3.txt", "r")

x=0
y=0
my_dict={(0,0):1}


for i in f.read():
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
