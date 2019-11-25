import csv

f = open("FS.csv", "w")

with open('testFS.csv', 'r') as content_file:
    next(content_file)
    content = content_file.read()
    f.write(content)


timestamp = []
readings = []

reader = csv.DictReader(open("FS.csv"))
print(reader.fieldnames)

for raw in reader:
    if raw.get('Record Type') == '1':
        timestamp.append(raw.get('Meter Timestamp'))
        readings.append(raw.get('Scan Glucose(mmol/L)'))

    else:
        timestamp.append(raw.get('Meter Timestamp'))
        readings.append(raw.get('Historic Glucose(mmol/L)'))

