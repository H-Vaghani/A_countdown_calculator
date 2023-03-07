import datetime

# method for day
def day():
    while True:
        x = input("Enter the Day between 1 to 31: ")
        try:
            day = int(x)
            if day < 1 or day > 31: # check the day is in between 1 to 31  
                print("Between 1 to 31")
            elif day == float: # check for float number
                print("Day cannot be in Float")
            else:
                break
        except ValueError:
            print("Input Invalid")
    return day      

#method for month  
def month():
    while True:
        m = input("Enter the month Between 1 To 12 ")
        try:
            month = int(m)
            if month < 1 or month > 12:
                print("Between 1 to 12")
            elif month == float:
                print("month cannot be in Float")
            else:
                break
        except ValueError:
            print("Input Invalid")
    return month

#method for year
def year():
    while True:
        y = input("Enter the year: ")
        xx = datetime.datetime.now()
        try:
            year = int(y)
            if year == float:
                print("Year cannot be in Float")
            elif year > xx.year:
                print("The year cannot Excessed current year")
            elif year < 1:
                print("Year cannot be in Negtive")
            else:
                break
        except ValueError:
            print("Input Invalid")
    return year

#method to find gap between to dates
def result():
    days = day()
    months = month()
    years = year() 

    print("To Enter another date")

    dd = day()
    mm = month()
    yyyy = year()
    x = datetime.date(years,months,days)
    y = datetime.date(yyyy,mm,dd)
    newdate = x - y
    return newdate

print("The time gap between is",abs(result()))

