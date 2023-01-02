import re
fh = open("regex_sum_1706544.txt")
l = fh.read()

y =  re.findall('[0-9]+', l)
count = 0
for i in y:
    a = int(i)
    count += a
print(count)
#print( sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] ) )

#close file 
fh.close()

