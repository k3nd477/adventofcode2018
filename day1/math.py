#!/usr/bin/python

f=open("numbers.txt", "r")

list = []

for o in list:
    print(o)

n = 0;

f1 = f.readlines()
for x in f1:
    if isinstance(x, str):
        n = n + int(x)
        print(n)
        if n in list:
            print(n)
        else:
            list.append(n)
    else:
        print(x)
