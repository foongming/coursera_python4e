timeDistribution = dict()
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

for line in fh:
    l = line.split()

    if len(l) <3 or l[0] != 'From':
        continue
    else:
        tmp1 = l[5]
        hour = tmp1[:2]
        timeDistribution[hour] = timeDistribution.get(hour,0) +1

#dictionaries can now be sorted
sorted_hours = sorted(timeDistribution.items(), key = lambda kv: kv[0])

sorted_wo_lambd = sorted([(k,v) for k,v in timeDistribution.items()])

#for k,v in sorted_hours:
#    print(k,v)

#for a,b in sorted_wo_lambd:
#    print(a,b)

for k,v in sorted(timeDistribution.items()):
    print(k,v)