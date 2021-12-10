log_file = open("um-server-01.txt")


def sales_reports(log_file): #defines the function that takes in the file
    for line in log_file: #for each line in the log_file file that is opened up
        line = line.rstrip() #takes off the trailing spaces
        day = line[0:3] #sets a variable day equal to the first word in line 
        if day == "Mon": #if the variable day equals the string of monday
            print(line) #display that line


sales_reports(log_file)

def overTen(log_file):
    for line in log_file:
        newArr = line.split(':')
        if int(newArr[0]) >= 10:
            print(line)

overTen(log_file)