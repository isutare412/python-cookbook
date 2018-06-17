from datetime import datetime, timedelta


def get_previous_day(
        dayname: 'string',
        start_date: 'datetime'=None,
        ) -> 'datetime':

    WEEK_DAYS = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday',
    ]

    if start_date is None:
        start_date = datetime.today()

    daynum = start_date.weekday()
    daynum_target = WEEK_DAYS.index(dayname.lower())
    days_ago = (7 + daynum - daynum_target) % 7

    if days_ago == 0:
        days_ago = 7

    return start_date - timedelta(days=days_ago)


if __name__ == '__main__':
    print(get_previous_day('SATURDAY'))
