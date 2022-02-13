log_file = open("um-server-01.txt") #creating a variable called log_file which = the .txt file


def sales_reports(log_file): #def = defining a function, named sales_reports, attached to the log file which refers to the txt file
    for line in log_file: #for loop, running a for loop on the file
        line = line.rstrip() #rstrip returns a copy of the string with trailing characters removed
        day = line[0:3] #tells python that day is located at this line (location) in the file
        if day == "Mon": #if conditional loop statement, so IF the day is Mon then..
            print(line) #print out the results of our function as defined above


sales_reports(log_file) #run our function on log_file which runs it on .txt file

