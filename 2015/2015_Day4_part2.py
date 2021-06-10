'''
--- Part Two ---
Now find one that starts with six zeroes.
'''

import hashlib

f = open("C:\\Users\Kevin\github\AdventofCode_new\\2015_4.txt", "r")
data=[]


for i in f.readlines():
    data.append(i.strip())

i=0
while True:
    i+=1
    testing_str=data[0]+str(i)
    encoding=testing_str.encode('utf-8')
    m=hashlib.md5(encoding).hexdigest()

    if m[:6]=="000000":
        print(i)
        break
