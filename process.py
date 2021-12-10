log_file = open("um-server-01.txt")


def sales_reports(log_file): #defines the function that takes in the file
    for line in log_file: #for each line in the log_file file that is opened up
        line = line.rstrip() #takes off the trailing spaces
        day = line[0:3] #checks the first three characters to see if the day is ___"
        if day == "Mon": #if the variable day equals the string of monday
            print(line) #display that line


sales_reports(log_file)

def print_melons(log_file):
    for line in log_file:
        values = line.rstrip().split(' ')
        total_melons = int(values[2])
        if total_melons > 10:
            print(total_melons)

    

print_melons(log_file)