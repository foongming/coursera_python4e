coders = {} 

fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
    l = line.split()

    if len(l) <3 or l[0] != 'From':
        continue
    else:
        email = l[1]
        coders[email] = coders.get(email,0) +1

bigcount = None
bigword = None 

for word,count in coders.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count 

print(bigword, bigcount)
