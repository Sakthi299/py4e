# mbox-short.txt

fname = input("Enter file name: ")
fh = open(fname)
sum_value = 0 
count = 0 
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    #print(line)
    count += 1
    pos = line.find(':')
    sum_value += float(line[pos+1:-1])

print("Average spam confidence:", sum_value/count)
