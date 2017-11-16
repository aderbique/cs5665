import os, sys, csv, re
from os import listdir
from SummaryStatistics import SS

def create_lists(filename):
    file = open(filename)
    num_lines = sum(1 for line in open(filename))
    print(num_lines)
    #users = [None]*(num_lines-1)
    #sessions = [None]*(num_lines-1)
    #events = [None]*(num_lines-1)

    users = []
    sessions = []
    events = []
    
    count = -1
    for line in file:
        if count > -1:
            parts = line.split(',')
            time = int(re.search("(\d\d\d\d\d\d)(\d\d)",parts[0]).group(1))
            print(time)
            #users[count] = parts[1]
            #sessions[count] = parts[2]
            #events[count] = parts[3].rstrip('\n')

            users.append(int(parts[1]))
            sessions.append(int(parts[2]))
            events.append(int(parts[3].rstrip('\n')))
            #time,users[count],sessions[count],events[count] = line.split(',')
        count = count + 1
    file.close()
    return users, sessions, events

def write_summary(filename, date,d,summ_type):
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
        file = open(filename,append_write)
        file.write('Date,Summary Type,Count,Sum,Min,Max,Median,Mode,Mean,Q1,Q3,Variance,StdDev,Range,IQR')
        file.close()

    file = open(filename,append_write)
    file.write(date + ',' + summ_type + ',' + str(d[0]) + ',' + str(d[1]) + ',' + str(d[2]) + ',' + str(d[3]) + ',' + str(d[4]) + ',' + str(d[5]) + ',' + str(d[6]) + ',' + str(d[7]) + ',' + str(d[8]) + ',' + str(d[9]) + ',' + str(d[10]) + ',' + str(d[11]) + ',' + str(d[12]) + '\n')
    #file.write(csv + ',' + summ_type + ',' + d['Count'] + ',' + d['Sum'] + ',' + d['Min'] + ',' + d['Max'] + ',' + d['Median'] + ',' + d['Mode'] + ',' + d['Mean'] + ',' + d['Q1'] + ',' + d['Q3'] + ',' + d['Variance'] + ',' + d['StdDev'] + ',' + d['Range'] + ',' + d['IQR'] + '\n')
    file.close() 


        
    
#day_user,day_session,day_event = create_lists("OSSUsersSessionsEventsByDay20160101-20170930.csv")

#day_user = SS(day_user)
#day_session = SS(day_session)
#day_event = SS(day_event)

#write_summary(time,'day_summary.csv',day_user)
#write_summary(time,'day_summary.csv',day_session)
#write_summary(time,'day_summary.csv',day_event)

def write_to_file(filename,line):
    #print('I am called')
    if os.path.exists(filename):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not
        file = open(filename,append_write)
        file.write('Date,Users,Sessions,Total Events\n')
        file.close()
        append_write = 'a'

    file = open(filename,append_write)
    file.write(line)
    file.close()


def split_files(filename):
    file = open(filename)
    num_lines = sum(1 for line in open(filename))
    #print(num_lines)
    #users = [None]*(num_lines-1)
    #sessions = [None]*(num_lines-1)
    #events = [None]*(num_lines-1)
    count = -1
    for line in file:
        if count > -1:
            parts = line.split(',')
            time = int(re.search("(\d\d\d\d\d\d)(\d\d)",parts[0]).group(1))
            name_of_file = str(time) + '.csv'
            print(time)
            write_to_file(name_of_file,line)
            #time,users[count],sessions[count],events[count] = line.split(',')
        count = count+1
    file.close()

#split_files("OSSUsersSessionsEventsByDay20160101-20170930.csv")

def find_csv_filenames(suffix=".csv" ):
    filenames = listdir(os.curdir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]

dirs = find_csv_filenames()


for csv in dirs:
    users, sessions, events = create_lists(csv)
    write_summary('prob5_results.csv',csv,users,'Users')
    write_summary('prob5_results.csv',csv,sessions,'Sessions')
    write_summary('prob5_results.csv',csv,events,'Events')
    
