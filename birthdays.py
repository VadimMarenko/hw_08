from datetime import datetime, timedelta
from collections import defaultdict

DAY_OF_WEEK = {0: "Monday",
               1: "Tuesday",
               2: "Wednesday",
               3: "Thursday",
               4: "Friday"}

users = [{"name": "Jason", "birthday": datetime(1990, 6, 28)},
        {"name": "Colleen", "birthday": datetime(1996, 6, 30)},        
        {"name": "Rodney", "birthday": datetime(2001, 7, 5)},
        {"name": "Thomas", "birthday": datetime(1976, 6, 27)},
        {"name": "Douglas", "birthday": datetime(1986, 7, 1)},                
        {"name": "Michael", "birthday": datetime(2000, 6, 30)},
        {"name": "Christina", "birthday": datetime(1964, 6, 29)},
        {"name": "Susan", "birthday": datetime(1984, 7, 2)},
        {"name": "Wendy", "birthday": datetime(1995, 6, 28)},
        {"name": "Jason", "birthday": datetime(1994, 7, 5)},
        {"name": "Jeffrey", "birthday": datetime(1964, 7, 3)},
        {"name": "James", "birthday": datetime(1968, 7, 2)},        
        {"name": "Mary", "birthday": datetime(1979, 7, 1)},
        {"name": "Karen", "birthday": datetime(1975, 6, 27)},
        {"name": "Loretta", "birthday": datetime(1985, 7, 3)},
        {"name": "Leah", "birthday": datetime(1993, 6, 29)},
        {"name": "Steven", "birthday": datetime(1985, 7, 2)}]

def get_birthdays_per_week(users):
    result = defaultdict(list)
    date_now = datetime.now().date()
    date_last = date_now + timedelta(days = 6)
    current_year = datetime.now().year
    for item in users:
        if isinstance(item["birthday"], datetime):
            bd = item["birthday"].date()
            bd = bd.replace(year=current_year)
            if  date_now <= bd <= date_last:
                if bd.weekday() in (5, 6):
                    result[0].append(item["name"])
                else:
                    result[bd.weekday()].append(item["name"])
    
    for i in range(5):
        if not result[i]:
            continue
        else:
            print(f"{DAY_OF_WEEK[i]}: {', '.join(result[i])}")
    
def main():
    try:
        if len(users) == 0:
            return "The list is empty"
        get_birthdays_per_week(users)
    except NameError as er:
        print(f"{er}")
 
if __name__ == "__main__":
    main()

