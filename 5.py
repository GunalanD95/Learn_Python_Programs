import csv

with open('Guna.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    

    
    writer.writerow(['Name', 'College', 'Age', 'Email','Phone.no'])
    writer.writerow(['Messi', 'Chile Clg','32', 'Messi1991@gmail.com', '123'])
    writer.writerow(['Ronaldo', 'Argentina Clg','34', 'Ronaldo1995@gmail.com', '456'])
    writer.writerow(['Isco', 'Brazil Clg','27', 'Isco1985@gmail.com', '789'])
    writer.writerow(['Bale',  'England Clg','30','Bale1975@gmail.com','1011'])
    writer.writerow(['Xavi', 'Portgual Clg','36', 'Xavi1985@gmail.com', '1213'])
    writer.writerow(['Pique', 'Germany Clg','32', 'Pique1987@gmail.com','1544'])
    writer.writerow(['Coutinho', 'LA Clg','27', 'Coutinho1991@gmail.com', '8787'])
    writer.writerow(['Suarez', 'Rosario Clg','32', 'Saurez1995@gmail.com', '9748'])
    writer.writerow(['Iniesta', 'Italy Clg','35', 'Iniesta1985@gmail.com', '2145'])
    writer.writerow(['Busquets', 'India Clg','31', 'Busquets1985@gmail.com', '11287'])
    writer.writerow(['Neymar', 'Netherlands Clg','27', 'Neymar1985@gmail.com', '4578'])

with open('Guna.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['Age'], row['College'])
