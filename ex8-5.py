fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
emails = []

#modified submisiion after solution review 
for line in fh:
    line.rstrip()
    l = line.split()
#guardian in a compound code 
    if len(l) <3 or l[0] != 'From':
        continue
    else:
        count += 1
        email = l[1]
        emails.append(email)

"""
#original submission
for line in fh:
    line.rstrip()
    l = line.split()
    if 'From' in l:
        count += 1
        email = l[1]
        emails.append(email)
    else:
        continue
"""
for e in emails:
    print(e)

print("There were", count, "lines in the file with From as the first word")