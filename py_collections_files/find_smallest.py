# setting flag
smallest_so_far = None

# iterate values in list
for the_num in [6,9,14,2,25,30]:
    if smallest_so_far is None:
        smallest_so_far = the_num
    elif the_num < smallest_so_far:
        smallest_so_far = the_num

print('The smallest number is ',smallest_so_far)