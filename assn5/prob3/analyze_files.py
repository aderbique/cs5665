import os, sys, csv
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
            time = int(parts[0])
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

def write_summary(fn,dictionary):
    w = csv.writer(open(fn, "wb"))
    for key, val in dictionary.items():
        w.writerow([key,val])
    
day_user,day_session,day_event = create_lists("OSSUsersSessionsEventsByDay20160101-20170930.csv")
hour_user,hour_session, hour_event = create_lists("OSSUsersSessionsEventsByHour20160101-20170930.csv")

day_user = SS(day_user)
day_session = SS(day_session)
day_event = SS(day_event)

hour_user = SS(hour_user)
hour_session = SS(hour_session)
hour_event = SS(hour_event)

write_summary('day_user.csv',day_user)
write_summary('day_session.csv',day_session)
write_summary('day_event.csv',day_event)
write_summary('hour_user.csv',hour_user)
write_summary('hour_session.csv',hour_session)
write_summary('hour_event.csv',hour_event)
#print(day_user)
