def format_phone_number(numbers_list):
    area_code = ''.join(map(str, numbers_list[:3]))
    first_part = ''.join(map(str, numbers_list[3:6]))
    last_part = ''.join(map(str, numbers_list[6:]))
    return f'({area_code}) {first_part}-{last_part}'


if __name__ == '__main__':
    print(format_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
    print(format_phone_number([5, 1, 9, 5, 5, 5, 4, 4, 6, 8]))
    print(format_phone_number([3, 4, 5, 5, 0, 1, 2, 5, 2, 7]))
