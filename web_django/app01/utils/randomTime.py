import random
import datetime


def random_date():
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 8, 1)
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_seconds = random.randint(0, 86400)  # Seconds in a day
    return start_date + datetime.timedelta(days=random_days, seconds=random_seconds)
