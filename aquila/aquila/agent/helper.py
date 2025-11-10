import pytz, datetime

def get_timezone():
    timezone = pytz.timezone('Asia/Jakarta')
    return timezone

def get_time_area(timezone):
    return datetime.datetime.now(timezone)

def get_date_and_time():
    timezone = get_timezone()
    times_area = get_time_area(timezone)
    format_date = "%Y-%m-%d %H:%M:%S"
    return times_area.strftime(format_date)
