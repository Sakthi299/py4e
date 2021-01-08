largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done" : break
        num = int(num)
        #print(num)
        if largest is None:
            largest = num
        elif largest < num:
            largest = num 
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
    
    except:
        print('Invalid input')
    

print("Maximum is",largest)
print("Minimum is",smallest)