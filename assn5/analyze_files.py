import os, sys
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
            time = parts[0]
            #users[count] = parts[1]
            #sessions[count] = parts[2]
            #events[count] = parts[3].rstrip('\n')

            users.append(parts[1])
            sessions.append(parts[2])
            events.append(parts[3].rstrip('\n'))
            #time,users[count],sessions[count],events[count] = line.split(',')
        count = count + 1
    file.close()
    return users, sessions, events
    
day_user,day_session,day_event = create_lists("OSSUsersSessionsEventsByDay20160101-20170930.csv")
hour_user,hour_session_hour_event = create_lists("OSSUsersSessionsEventsByHour20160101-20170930.csv")


day_user = SS(day_user)
day_session = SS(day_session)
day_event = SS(day_event)

hour_user = SS(hour_user)
hour_session = SS(hour_session)
hour_event = SS(hour_event)
