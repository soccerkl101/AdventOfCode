'''

--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

'''

#used https://stackoverflow.com/questions/49138673/find-repeating-characters-in-a-string-using-regex to help with repeating letters

import re

f = open("C:\\Users\Kevin\github\AdventofCode_new\\2015_5.txt", "r")
data=[]


for i in f.readlines():
    data.append(i.strip())
print(data)


print(len([x for x in data if (re.search(r'([aeiou].*){3}', x) and re.search(r'(.)\1', x) and not re.search(r'ab|cd|pq|xy', x))]))
