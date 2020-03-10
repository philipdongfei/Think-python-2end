from datetime import datetime

def weekday():
    today = datetime.today()
    print(today)
    print(today.strftime("%A"))

def nextbday():
    s = input('Enter your birthday in mm/dd/yyyy format: ')
    bday = datetime.strptime(s, '%m/%d/%Y')
    today = datetime.today()
    next_bday = bday.replace(year=today.year)
    if next_bday < today:
        next_bday = next_bday.replace(year=today.year+1)
    print(next_bday)
    until_next_bday = next_bday - today
    print(until_next_bday)

def doubleday():
    s = input('Enter one birthday in mm/dd/yyyy format: ')
    bday1 = datetime.strptime(s, '%m/%d/%Y')
    s = input('Enter other birthday in mm/dd/yyyy format: ')
    bday2 = datetime.strptime(s, '%m/%d/%Y')
    d1 = min(bday1, bday2)
    d2 = max(bday1, bday2)
    dd = d2 + (d2-d1)
    print(dd)

def main():
    weekday()
    nextbday()
    doubleday()

if __name__ == '__main__':
    main()

