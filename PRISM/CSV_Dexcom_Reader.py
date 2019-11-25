import csv

reader = csv.DictReader(open("testDexcom.csv"))
timestamp = []
readings = []
baggedReadings = []
baggedTimestamps = []
for raw in reader:
    if raw.get('Timestamp (YYYY-MM-DDThh:mm:ss)') != '':
        timestamp.append(raw.get('Timestamp (YYYY-MM-DDThh:mm:ss)'))
        readings.append(raw.get('Glucose Value (mmol/L)'))

print(len(timestamp), len(readings))


def bagTime():
    global timestamp
    iterator = 0
    totalBaggedItems = 0
    length = len(timestamp)

    while True:
            for elements in range(iterator, len(timestamp)):
                try:
                    count = 0
                    baggingDateSample = []
                    baggingTimeSample = []
                    while count < 3:
                        baggingDateSample.append(timestamp[iterator].split('T')[0])
                        baggingTimeSample.append(timestamp[iterator].split('T')[1])
                        count += 1
                    baggedTimestamps.append(formatDate(baggingDateSample, baggingTimeSample))
                    print(formatDate(baggingDateSample, baggingTimeSample))
                    iterator += 3
                    totalBaggedItems += 1
                except IndexError:
                    break
            if iterator >= len(timestamp):
                break
    print(totalBaggedItems)


def formatDate(dateSamples, timeSamples):
    formated_date = averageDate(dateSamples)
    average_time = averageTime(timeSamples)
    return formated_date + " " + average_time


def averageDate(dateSamples):
    Sum = 0
    for i in range(0,len(dateSamples)):
        Sum += (int(dateSamples[i].split('-')[0])*365) + (int(dateSamples[i].split('-')[1])*30)+ int(dateSamples[i].split('-')[1])
    avg = Sum / len(dateSamples)
    month = int(avg % 365 // 30)
    days = int(avg % 365 % 30)
    year = int(avg // 365)
    date = str(year) + '-' + str(month) + '-' + str(days)
    return date


def averageTime(timeSamples):
    Sum = 0
    for i in range(0, len(timeSamples)):
        Sum += (int(timeSamples[i].split(':')[0]) *3600) + (int(timeSamples[i].split(':')[1]) *60) + int(timeSamples[i].split(':')[2])
    avg = Sum // len(timeSamples)
    hours = avg // 3600
    mins = (avg % 3600) // 60
    secs = (avg % 3600) % 60
    time = str(hours) + ":" + str(mins) + ":" + str(secs)
    return time


def bagReadings():
    global readings
    iterator = 0
    totalBaggedItems = 0
    length = len(timestamp)
    print(length)

    while True:
        for elements in range(iterator, len(timestamp)):
            try:
                count = 0
                baggingReadingSample = []
                while count < 3:
                    if readings[iterator] == '':
                        pass
                    elif readings[iterator] == 'High':
                        baggingReadingSample.append(24*18)
                    elif readings[iterator] == 'Low':
                        baggingReadingSample.append(35)
                    else:
                        baggingReadingSample.append(int(float(readings[iterator])*18))
                    count += 1
                    iterator += 1
                baggedReadings.append(averageReading(baggingReadingSample))
                print(averageReading(baggingReadingSample))

                totalBaggedItems += 1
            except IndexError:
                break
        if iterator >= len(timestamp):
            break
    print(totalBaggedItems)


def averageReading(readingSamples):
    sum = 0
    for i in readingSamples:
        sum += i
    avg = sum // len(readingSamples)
    return avg


bagReadings()
bagTime()


