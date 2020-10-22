import csv
with open('Guna.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['Age'], row['College'])
