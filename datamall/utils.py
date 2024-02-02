import datetime


def calculate_time(time: str) -> str | None:
    """Calculate the time difference"""
    current_time = datetime.datetime.now()
    next_timing = datetime.datetime.strptime(time, "%Y-%m-%dT%H:%M:%S%z").replace(
        tzinfo=None
    )

    time_difference = next_timing - current_time
    time_difference = round(time_difference.total_seconds() / 60)

    if time_difference <= 1:
        return "Arr"
    elif time_difference >= 1:
        return str(time_difference)
    else:
        return None
