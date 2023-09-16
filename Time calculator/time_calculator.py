def add_time(start, duration, start_day=None):

    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if am_pm == "PM":
        start_hour += 12

    duration_hour, duration_minute = map(int, duration.split(':'))

    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60

    days_later = total_minutes // 60 // 24

    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(start_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    if new_hour >= 12:
        new_am_pm = "PM"
        if new_hour > 12:
            new_hour -= 12
    else:
        new_am_pm = "AM"
        if new_hour == 0:
            new_hour = 12

    result = f"{new_hour}:{new_minute:02d} {new_am_pm}"

    new_time=result
    if start_day:
        new_time += f", {new_day}"
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time
