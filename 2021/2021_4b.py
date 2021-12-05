"""
--- Part Two ---
On the other hand, it might be wise to try a different strategy: let the giant squid win.

You aren't sure how many bingo boards a giant squid could play at once, so rather than waste time counting its arms, the safe thing to do is to figure out which board will win last and choose that one. That way, no matter which boards it picks, it will win for sure.

In the above example, the second board is the last to win, which happens after 13 is eventually called and its middle column is completely marked. If you were to keep playing until this point, the second board would have a sum of unmarked numbers equal to 148 for a final score of 148 * 13 = 1924.

Figure out which board will win last. Once it wins, what would its final score be?
"""

f = open("C:\\Users\socce\github\AdventOfCode\\2021\\2021_4b-input.txt", "r")

picks = []
boards = []
tmp=[]
t=False
last=False
count=0

for i in f:
    i = i.strip()
    if len(picks) == 0:
        picks=[int(x) for x in i.split(',')]
    else:
        if i:
            tmp.append([int(x) for x in i.split()])
        else:
            if tmp:
                boards.append(tmp)
            tmp=[]
boards.append(tmp)

for i in range(5,len(picks)+1):
    picked=picks[:i]
    for j in boards:
        for y in range(5):
            row=set(j[y])
            column=set([line[y] for line in j])
            if last:
                if row.issubset(picked) or column.issubset(picked):
                    for rows in j:
                        for numbs in rows:
                            if numbs not in picked:
                                count+=numbs
                    print(count*picked[-1])
                    t=True
                    break
            elif row.issubset(picked) or column.issubset(picked):
                boards.remove(j)
                if len(boards)==1:
                    last=True
                break
        if t:
            break
    if t:
        break
