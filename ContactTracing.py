import csv
from datetime import datetime

def date_converter(date):
    # Convert date into the same format to avoid confusion
    converted_date = datetime.strptime(date, '%m/%d/%Y').strftime('%d %b %Y')
    return converted_date

def search_people(address, date, patient):
    with open('contacts.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            the_date = date_converter(row['Date'])
            person = row['User']
            if row['Address'] == address and the_date == date and row['User'] != patient:
                print(f'{person} should stay at home for next 10 days due to the trip to {address} on {date}')

patient = input('The person who was tested positive: ')
test_date = input('When was the test? ')
test_date = date_converter(test_date)

with open('contacts.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        date = date_converter(row['Date'])
        if row['User'] == patient and date == test_date:
            address = row['Address']
            search_people(address, test_date, patient)
