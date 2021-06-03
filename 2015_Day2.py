f = open("C:\\Users\Kevin\Desktop\Adventofcodestuff\\2015_2.txt", "r")

total_paper=0
total_ribbon=0

for i in f.readlines():
    #print(i)
    l=int(i.split("x")[0])
    w=int(i.split("x")[1])
    h=int(i.split("x")[2])
    #print(l, w, h)
    surfacearea=(2*l*w + 2*w*h + 2*h*l)

    smallestarea=min(l*w, l*h, w*h)

    total_paper += surfacearea+smallestarea

    allsides=[l,w,h]
    smallest_side=min(allsides)


    allsides.remove(smallest_side)
    second_smallest=min(allsides)
    total_ribbon+=((smallest_side * 2 + second_smallest * 2) + (l*w*h))


print(total_paper)
print(total_ribbon)
