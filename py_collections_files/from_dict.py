# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of 
# the number of times they appear in the file. 

fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"

fh = open(fname)
msg = dict()
for line in fh:
    if not line.startswith('From '):
        continue
    addr = line.split()[1]
    #count += 1
    msg[addr] = msg.get(addr, 0) +1

large_value = -1
large_key = None
for k,v in msg.items():
    print(k,v)
    if v > large_value:
        large_value = v
        large_key = k

max_key = max(msg, key=msg.get)
max_value = msg[max_key]
print(max_key,max_value)