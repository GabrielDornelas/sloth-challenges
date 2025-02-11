from datetime import datetime

def hours_passed(t1, t2):
    fmt = "%I:%M %p"
    hour1 = datetime.strptime(t1, fmt)
    hour2 = datetime.strptime(t2, fmt)
    diff = (hour2 - hour1).total_seconds() / 3600
    if diff == 0:
        return 'no time passed'

    return f"{int(diff)} hours"


if __name__ == '__main__':
    print(hours_passed("3:00 AM", "9:00 AM"))
    print(hours_passed("2:00 PM", "4:00 PM"))
    print(hours_passed("1:00 AM", "3:00 PM"))
    print(hours_passed("4:00 PM", "4:00 PM"))
