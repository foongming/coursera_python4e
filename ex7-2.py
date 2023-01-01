# Use the file name mbox-short.txt as the file name
list = []
running_count = 0 
count_lines = 0

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        pos = line.rfind(' ')
        data = float(line[pos+1:])
        list.append(data)
        count_lines = count_lines +1
        running_count += data
    #print(running_count)
average = running_count / count_lines
print("Average spam confidence:", average)

