from datetime import date, timedelta
import calendar


def get_month_range(given_date: 'date'=None):
    '''Return [start_date, end_date) of a month
    that the given_date is included
    '''
    if given_date is None:
        given_date = date.today()
    start_date = given_date.replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


if __name__ == '__main__':
    sdate, edate = get_month_range()

    def date_range(start, stop, step):
        while start < stop:
            yield start
            start += step
    for d in date_range(sdate, edate, timedelta(days=1)):
        print(d)

    print(sdate, edate, sep=' ~ ')
