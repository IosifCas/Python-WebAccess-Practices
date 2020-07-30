# Program using Regular Expressions to find numbers and add them 
import re

fname = input('Enter file name:')
try :
    fhand = open(fname)
except :
    print('File', fname, 'could not be opened')
    quit()

num = 0
s = 0
i = 0
for line in fhand :
    line = line.rstrip()
    if re.search('[0-9]+\S+?', line) :
        n = re.findall('[0-9]+\S?', line)
        print(n)
        i = 0
        for part in n :
            part = n[i]
            print(part)
            try :
                num = int(part)
            except : continue    
            i = i+1
            s = s + num
print('Sum of values =', s)