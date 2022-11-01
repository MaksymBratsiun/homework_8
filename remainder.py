from datetime import datetime, timedelta


users = {'Dima': '1996-11-05',
         'Valia': '1996-11-06',
         'Viktor': '1996-11-07',
         'Natasha': '1996-11-08',
         'Vlad': '1996-11-09',
         'Igor': '1996-11-10',
         'Danilo': '1996-11-10',
         'Lida': '1996-11-11',
         'Ivan': '1996-11-11'
         }


def concvert_from_iso(users):
    users_iso_list = {}
    for item in users:
        day_datetime = datetime.fromisoformat(users[item])
        users_iso_list.update({item: day_datetime})
    return users_iso_list


def get_birthdays_per_week(birthday_list):
    birthdays = []
    birthdays.append(on_monday(birthday_list))
    birthdays.extend(on_other_days(birthday_list))
    for item in birthdays:
        print(item)


def main():
    datetime_users = concvert_from_iso(users)
    get_birthdays_per_week(datetime_users)


def next_monday():
    today_date = datetime.now()
    weekday_day = today_date.weekday()
    return today_date + timedelta(days=7-weekday_day)


def on_monday(birthday_list):
    monday_name = 'Monday: '
    names = []
    for name in birthday_list:
        if datetime.strftime(birthday_list[name], '%d %b') == datetime.strftime(next_monday(), '%d %b'):
            names.append(name)
        elif datetime.strftime(birthday_list[name], '%d %b') == datetime.strftime(next_monday() - timedelta(days=1), '%d %b'):
            names.append(name)
        elif datetime.strftime(birthday_list[name], '%d %b') == datetime.strftime(next_monday() - timedelta(days=2), '%d %b'):
            names.append(name)
    if names:
        names_str = ', '.join(names)
        monday_str = monday_name + names_str
        return monday_str
    else:
        return ''


def on_other_days(birthday_list):
    current_day_name = ['Tuesday: ', 'Wednesday: ', 'Thursday: ', 'Friday: ']
    curent_list = []
    for i in range(1, 5):
        names_on_day = []
        names_on_day_str = ''
        for name in birthday_list:
            if datetime.strftime(birthday_list[name], '%d %b') == datetime.strftime(next_monday() + timedelta(days=i), '%d %b'):
                names_on_day.append(name)
        names_on_day_str = ', '.join(names_on_day)
        if names_on_day_str:
            names_str = current_day_name[i-1] + names_on_day_str
            curent_list.append(names_str)
    return curent_list


if __name__ == '__main__':
    main()
