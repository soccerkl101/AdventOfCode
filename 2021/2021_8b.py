"""
--- Day 8: Seven Segment Search ---
You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg
So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly. Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1, so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f). For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input). Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
cdfeb fcadb cdfeb cdbaf
(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are). The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections. Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on. Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits. Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |
fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |
fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |
cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |
efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |
gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |
gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |
cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |
ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |
gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |
fgae cfgab fg bagce
Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits. Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?
"""
f = open("C:\\Users\socce\github\AdventOfCode\\2021\\2021_8b-input.txt", "r")

patterns=[]
display = []
for i in f:
    i=i.strip().split("|")
    patterns.append(i[0].strip())
    display.append(i[1].strip())

count=0
iteration=0
for i in patterns:
    dict={}
    misses=[]
#    print(i.split(" "))
    for x in i.split(" "):
        tmp=''.join(sorted(x))
        #print(''.join(sorted(x)))
        if len(x) == 2:
            dict[tmp]=1
        elif len(x) == 4:
            dict[tmp]=4
        elif len(x) == 3:
            dict[tmp]=7
        elif len(x) == 7:
            dict[tmp]=8
        else:
            misses.append(tmp)
    for x in misses:
        if len(x) == 5:
            flag = 0
            for i in list(dict.keys())[list(dict.values()).index(7)]:
                if i in x:
                    flag+=1

            if flag == 3:
                dict[x]=3
                misses.remove(x)
    for x in misses:
        if len(x) == 6:
            flag = 0
            tmp = set()
            tmp.update(list(dict.keys())[list(dict.values()).index(4)], list(dict.keys())[list(dict.values()).index(3)])
            for i in tmp:
                if i in x:
                    flag+=1
            if flag == 6:
                dict[x]=9
                misses.remove(x)
    for x in misses:
        if len(x) == 6:
            flag = 0
            tmp = []
            for i in (list(dict.keys())[list(dict.values()).index(8)]):
                tmp.append(i)
            for i in (list(dict.keys())[list(dict.values()).index(7)]):
                tmp.remove(i)
            for i in tmp:
                if i in x:
                    flag+=1
            if flag == 4:
                dict[x]=6
                misses.remove(x)
    for x in misses:
        if len(x) == 5:
            flag = 0
            tmp = []
            tmp1= []
            for i in (list(dict.keys())[list(dict.values()).index(8)]):
                tmp.append(i)
            for i in (list(dict.keys())[list(dict.values()).index(9)]):
                tmp.remove(i)
            tmp="".join(tmp)
            for i in (list(dict.keys())[list(dict.values()).index(6)]):
                tmp1.append(i)
            tmp1.remove(tmp)
            for i in tmp1:
                if i in x:
                    flag+=1
            if flag == 5:
                dict[x]=5
                misses.remove(x)
    for x in misses:
        if len(x)==5:
            dict[x]=2
        else:
            dict[x]=0
#    print(dict)

    ouputvalues = []
    listnumber=[]
    print(display[iteration])
    ouputvalues=(display[iteration].split(" "))
    print(ouputvalues)
    for b in ouputvalues:
        print("".join(sorted(b)))
        listnumber.append(dict.get("".join(sorted(b))))
    iteration+=1
    strings=[str(integer) for integer in listnumber]
    tally=int("".join(strings))
    count+=tally
print(count)




#2, 3, 4, 7
"""
0 - 6 - FIND 5th/6th. only remaining 6 digit is this.
1 - 2 unique
2 - 5 - FIND 5th/6th. only remaining 5 digit is this.
3 - 5 - FIND FIRST. if 7's letters are in it and its 5 characters, then its 3
4 - 4 unique
5 - 5 - FIND FOURTH. 9's letters - 8's letters finds you E. 6's letters - E = 5's letters.
6 - 6 - FIND THIRD. 8's letters - 7's letters finds you BDEG. Of the remaining, only 6 has those characters.
7 - 3 unique
8 - 7 unique
9 - 6 - FIND SECOND. if 4's lettesr are in it, and 3's letters are in it and its 6 characters, then its 9

LETTER E = 9's letters - 8's letters.
"""
