import csv
from datetime import datetime

def search_people(address, date, patient):
    with open('contacts.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            person = row['User']
            if row['Address'] == address and row['Date'] == date and row['User'] != patient:
                converted_date = datetime.strptime(date, '%m/%d/%Y').strftime('%d %b %Y')
                print(f'{person} should stay at home for next 10 days due to the trip to {address} on {converted_date}')

patient = input('The person who was tested positive: ')
test_date = input('When was the test? ')


with open('contacts.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row['User'] == patient and row['Date'] == test_date:
            address = row['Address']
            search_people(address, test_date, patient)
