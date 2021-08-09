import random
from datetime import date, timedelta

sdate = date(2008, 1, 1)   
edate = date(2008, 12, 31)   

delta = edate - sdate
print(delta)
dates = []
for i in range(delta.days + 1):
    day = sdate + timedelta(days=i)
    dates.append(date.strftime(day, '%d %b'))

def match(number):
    date_sample = random.choices(dates, k = number)
    count = 0
    for date in date_sample:
        if date_sample.count(date) > 1:
            count += 1
            return count
    return count

def percentage(number):
    count = 0
    first_digit = 0
    counter = 0
    for i in range(100000):
        counter += 1
        count += match(number)
        if counter > 10000:
            first_digit += 1
            counter = 0
            print('{}0 000 iterations complete'.format(first_digit))
    percent = count / 100000 * 100
    return percent

def birthday_paradox():
    print('\nThe Birthday Paradox allows us to see what the percentage chance of any number of people having the \nsame birthday in a chosen number of people. We might be surprised by how high the likelihood is!')
    while True:
        number = input('\nHow many people would you like in your sample size? - Max 100 \n')
        if number.isdigit():
            number = int(number)
            if number <= 100 and number > 1:
                break
        print('Invalid response. Please input a number inbetween 2 and 100')
    return '{}%'.format(percentage(number))
    
print(birthday_paradox())