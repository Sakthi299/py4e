# pip install urllib

#Urllib is a package that collects several modules for working with URLs, such as:

#    urllib.request for opening and reading.
#    urllib.parse for parsing URLs
#    urllib.error for the exceptions raised
#    urllib.robotparser for parsing robot.txt files


from urllib import request, parse, error

try:
    file_handler = request.urlopen('http://data.pr4e.org/romeo.txt')
    #print(file_handler.read())
    for line in file_handler:
        print(line.decode().strip())
except Exception as e:
    print(str(e))