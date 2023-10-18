from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    week_days = {"Monday": [], "Tuesday": [], "Wednesday": [],
                 "Thursday": [], "Friday": []}
    today = datetime.today().date()
    print(f"today {today}")

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta = birthday_this_year - today
        delta_days = delta.days
        print(f"""Name: {name}, Birthday: {birthday_this_year},
               Days to birthday: {delta_days}""")

        if delta_days < 7:
            weekday = birthday_this_year.weekday()

            if weekday in [0, 5, 6]:
                week_days["Monday"].append(name)
            elif weekday == 1:
                week_days["Tuesday"].append(name)
            elif weekday == 2:
                week_days["Wednesday"].append(name)
            elif weekday == 3:
                week_days["Thursday"].append(name)
            elif weekday == 4:
                week_days["Friday"].append(name)

    for key, value in week_days.items():
        if value:
            print(f"{key}: {', '.join(value)}")


users = [
    {"name": "Ivan Diabin", "birthday": datetime(1997, 10, 21)},
    {"name": "Kate Zaichenko", "birthday": datetime(1992, 10, 18)},
    {"name": "Mick Jager", "birthday": datetime(1985, 10, 7)},
    {"name": "Henly Hensen", "birthday": datetime(1954, 1, 14)},
    {"name": "Zakhar Panaseyko", "birthday": datetime(1995, 9, 4)}
]

get_birthdays_per_week(users)
