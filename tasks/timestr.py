__all__ = (
    'seconds_to_str',
)


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    days = seconds // (60 * 60 * 24)
    if days:
        seconds -= 60 * 60 * 24 * days
        days = f'0{days}d' if days < 10 else str(days) + 'd'
    else:
        days = ''

    hours = seconds // (60 * 60)
    if hours or days:
        seconds -= 60 * 60 * hours
        hours = f'0{hours}h' if hours < 10 else str(hours) + 'h'
    else:
        hours = ''

    minutes = seconds // 60
    if minutes or days or hours:
        seconds -= 60 * minutes
        minutes = f'0{minutes}m' if minutes < 10 else str(minutes) + 'm'
    else:
        minutes = ''

    new_seconds = seconds % 60
    if new_seconds:
        new_seconds = f'0{new_seconds}s' if new_seconds < 10 else str(new_seconds) + 's'
    else:
        new_seconds = '00s'

    return days + hours + minutes + new_seconds




