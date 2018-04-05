'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime, timedelta
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()

#Checking the lines
# for line in loglines:
#     print(line)


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    relevant = line.split(" ")[1]
    # print(relevant)
    whole_date = relevant.split('T')[0]
    whole_time = relevant.split('T')[1]
    year = int(whole_date.split('-')[0])
    month = int(whole_date.split('-')[1])
    day = int(whole_date.split('-')[2])
    hour = int(whole_time.split(':')[0])
    minute = int(whole_time.split(':')[1])
    second = int(whole_time.split(':')[2])
    return datetime(year, month, day, hour, minute, second)



def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    events = []
    for line in loglines:
        #removing the period(.) and ('\n') from the line
        line = line[:-2]
        #Pick the last to words of the line to get the event.
        event = " ".join(line.split(' ')[-2:])
        # print(event)
        if event == SHUTDOWN_EVENT:
            events.append(convert_to_datetime(line))
    # print(events)
    if len(events) == 0:
        return timedelta(0)
    else:
        return events[-1] - events[0]
