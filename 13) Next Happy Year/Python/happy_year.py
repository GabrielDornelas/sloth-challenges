def happyYear(year):
    current = year
    while True:
        current += 1
        year_string = str(current)
        if len(year_string) == len(set(year_string)):
            return current


if __name__ == '__main__':
    inputs = [2017, 1990, 2021]
    for item in inputs:
        print(happyYear(item))
