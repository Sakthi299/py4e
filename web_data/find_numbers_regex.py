import re
added_value = 0
file_name = open("actual_data.txt", "r")
numbers =  re.findall('[0-9]+', file_name.read())
results = list(map(int, numbers))
for num in results:
    added_value+=num
print(added_value)
