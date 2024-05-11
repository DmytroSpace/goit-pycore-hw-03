from datetime import datetime

def get_days_from_today(date: str) -> int:
    current_date = datetime.today()
    try:
        
        date = datetime.strptime(date, "%Y-%m-%d")                       # parse str to date
        delta = current_date - date                                      # difference between 2 dates

        print(f"Різниця в днях між датами складає: {delta.days}")
        return delta.days
    
    except ValueError:                                                   # message if date format is incorrect
        print('Дата має бути введена у форматі "РРРР-ММ-ДД"')
        

get_days_from_today('2023-01-09')