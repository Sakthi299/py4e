# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#  You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end. 

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
count = 0
hours = dict()
inc_lst = list()
for line in fh:
    if not line.startswith('From '):
        continue

    # From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    #print(line.split()[5].split(':')[0])
    hr = line.split()[5].split(':')[0]
    hours[hr] = hours.get(hr,0)+1

for k,v in hours.items():
    inc_lst.append((k,v))

for i in sorted(inc_lst):
    print(i[0], i[1])