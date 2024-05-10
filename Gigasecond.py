from datetime import timedelta, datetime
GIGASECOND = 1e9


def add(moment: datetime) -> datetime:
    duration = timedelta(seconds = GIGASECOND)
    return moment + duration