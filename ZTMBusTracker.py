from requests import get
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

import json
import time

def rTimeFormat(tmie):
    return(str((tmie - timedelta(minutes=2)) + timedelta(seconds=13)).replace('0:', ''))

def cachedBusTimeParser():
    def getBusTimes():
        url = "https://www.ztm.poznan.pl/pl/rozklad-jazdy/XXX/XXX/XXX:XXX-XXX"
        r = get(url)
        soup = BeautifulSoup(r.text, 'html.parser')

        # Find all spans with class 'trip-details-minute' under td elements
        time_spans = soup.select('td.stop-hours-table__minutes span.trip-details-minute')

        # Extract and print the times
        bus_arrival_times = [span['data-hour'] for span in time_spans]
        return(bus_arrival_times)

    def saveCache(data, timestamp):
        cacheData = {
            'data': data,
            'timestamp': timestamp
        }
        with open('jdapCache.json', 'w') as file:
            json.dump(cacheData, file)

    def loadCache():
        try:
            with open('jdapCache.json', 'r') as file:
                cacheData = json.load(file)
                return cacheData['data'], cacheData['timestamp']
        except (FileNotFoundError, json.JSONDecodeError):
            return None, 0

    cacheData, last_timestamp = loadCache()
    
    currentTimestamp = int(time.time())

    if currentTimestamp - last_timestamp > 86400:  # 86400 seconds in a day
        # Fetch new data if the cache is more than a day old
        newData = getBusTimes()
        saveCache(newData, currentTimestamp)

    # Use the data as needed (replace this with your actual processing)
    cacheData, last_timestamp = loadCache()
    return(cacheData)

times = cachedBusTimeParser()

filteredTimes =[]
for i in range(len(times)):
    if i != 0:
        if (int(str(times[i]).split(':')[0])-int(str(times[i-1]).split(':')[0])) == -18:
            break
        else:
            filteredTimes.append(times[i])
    else:
        filteredTimes.append(times[i])

now = (datetime.now().strftime('%H:%M:%S'))

inFuture = []
# get times after the current time
for i in filteredTimes:
    if datetime.strptime(i, '%H:%M') > datetime.strptime(now, '%H:%M:%S'):
        inFuture.append(i)

futureFiltered = []
for i in inFuture:
    futureFiltered.append(datetime.strptime(i, '%H:%M') - datetime.strptime(now, '%H:%M:%S'))

futureFinal = []
for i in range(len(futureFiltered)):
    if i < 2:
        futureFinal.append(futureFiltered[i])

print(rTimeFormat(futureFinal[0]), rTimeFormat(futureFinal[1]))
