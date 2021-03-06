# Reading and Writing Files
# Creates a new file object and assigning it to a variable called file
# Current line assumes that the spider.txt file is in the same directory
file = open("module-two/week2/spider.txt")

# readline method reads a single line of a file
print(file.readline())
# readline method reads the second line of a file - each time the readline method is called, the file object updates the current position in the file
print(file.readline())
# read method, which reads from the current position until the end of the file instead of just one line
print(file.read())

# Opened file needs to be closed to conform the open-close approach
file.close()

# "with" keyword creates a block of code with the work that needs to be done with the file inside of it
# When "with" block is used, Python will automatically close the file
with open("module-two/week2/spider.txt") as file:
    print(file.readline())

# Iterates the file object like list or strings
# The file has a new line character at the end of each line
# When Python reads the file line by line, the line variable will always have a new line character at the end
with open("module-two/week2/spider.txt") as file:
    for line in file:
        print(line.upper())

# Empty lines can be avoided by using strip method
with open("module-two/week2/spider.txt") as file:
    for line in file:
        print(line.strip().upper())

# Iterates the file object by reading the file lines into a list
file = open("module-two/week2/spider.txt")
lines = file.readlines()
file.close
lines.sort()
print(lines)

# "with" block pattern takes the second argument which specifies in which mode the file should be opened as
with open("module-two/week2/novel.txt", "w") as file:
    file.write("It was a dark and stormy night")

# Managing Files and Directories
# os module provides a layer of abstraction between Python and the operating system
import os

# remove function deletes a file
os.remove("module-two/week2/novel.txt")

# rename function renames a file
# The first parameter to rename function is the old name of the file and the second is new name
os.rename("module-two/week2/spider.txt", "module-two/week-two/spider_rename.txt")
os.rename("module-two/week2/spider_rename.txt", "module-two/week-two/spider.txt")

# the OS path sub-module's exists function checks whether a file exist
print(os.path.exists("module-two/week2/spider_rename.txt"))

# getsize checks a file size and returns the file size in bytes
print(os.path.getsize("module-two/week2/spider.txt"))

# getmitime checks when the file was last modified and returns Unix timestamp
print(os.path.getmtime("module-two/week2/spider.txt"))

# datetime module provides a function to convert the Unix timestamp
import datetime
timestap = os.path.getmtime("module-two/week2/spider.txt")
print(datetime.datetime.fromtimestamp(timestap))

# abspath function takes a filename and turns it into an absolute path
print(os.path.abspath("spider.txt"))

# Directories
# getcwd function checks which current directory the Python program is executing
print(os.getcwd())

# mkdir function creates a directory
os.mkdir("module-two/week2/new_dir")

# chdir function changes a directory
os.chdir("module-two/week2/new_dir")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())

# rmdir function removes a directory
os.rmdir(os.path.abspath("new_dir"))

os.chdir("..")
print(os.getcwd())
# os.listdir function returns a list of all the files and sub-directories in a given directory
print(os.listdir("week2"))
dir = "week2"
os.mkdir("week2/another_new_dir")
for name in os.listdir(dir):
    # os.path.join creates the full path and it can be used to to check if the files are directory or not
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

os.rmdir("week2/another_new_dir")

# Reading CSV Files
import csv
f = open("week2/csv_file.txt")

# parses the file using the CSV module
csv_f = csv.reader(f)
for row in csv_f:
    # unpakcs the value from the CSV file
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()

# Write to csv file
hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)



# Reading and Writing CSV Files with Dictionaries
# DictReader turns each row of the data in a CSV file into a dictionary
with open ("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))

# DictWriter generates a CSV file from the contents of a list of dictionaries
users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
{"name": "Charlie Grey", "username": "greyc", "department": "Development" }]

keys = ["name", "username", "department"]

with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

os.remove("week2/by_department.csv")