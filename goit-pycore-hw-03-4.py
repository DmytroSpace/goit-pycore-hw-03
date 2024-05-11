from datetime import datetime, timedelta

def get_upcoming_birthday(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()      # parse datetime
        birthday_this_year = birthday_date.replace(year=today.year) 
        
        if birthday_this_year < today:                                              # if bd already was -> congrats next year
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_until_birthday = (birthday_this_year - today).days 

        
        if 0 <= days_until_birthday <= 7:                                           # if bd will be in 7 days
            if birthday_this_year.weekday() >= 5:                                   # if bd is on weekend
                
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday())) 
            
            upcoming_birthdays.append({"name": user["name"], \
            "congratulation_date": birthday_this_year.strftime('%Y-%m-%d')})        # add info to upcoming_birthdays if proper user finded
 
 

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Karl Buduar", "birthday": "1983.05.11"},
    {"name": "Jay Krakovic", "birthday": "1994.06.30"},
    {"name": "Ivan Mighty", "birthday": "1996.05.17"},
    {"name": "Monica Lineker", "birthday": "1989.04.22"},
    {"name": "Sara O'Conneli", "birthday": "1995.09.01"},
    {"name": "Sam Broker", "birthday": "1997.01.27"},
]

upcoming_birthdays = get_upcoming_birthday(users)
print("Список привітань на наступний тиждень:")
for birthday in upcoming_birthdays:
    print(birthday)
