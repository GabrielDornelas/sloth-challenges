def actualMemorySize(memory_size: str) -> str:
    '''
    This function takes the memory size as an argument and returns the actual memory size.

    Examples
    actualMemorySize("32GB")
    output = "29.76GB"

    actualMemorySize("2GB")
    output = "1.86GB"

    actualMemorySize("512MB")
    output = "476MB"

    Notes
    The actual storage loss on a USB device is 7% of the overall memory size!

    If the actual memory size was greater than 1 GB, round your result to two decimal places.

    If the memory size after adjustment is smaller then 1 GB, return the result in MB.

    For the purposes of this challenge, there are 1000 MB in a Gigabyte.

    Args:
        memory_size: The input string of memory in GB or MB.

    Returns:
        str: Actual memory size.
    '''
    actual_memory_size = ''
    unit = memory_size[-2:].upper()
    size = float(memory_size[:-2])
    if (unit == 'GB' and size >= 1) or (unit == 'MB' and size >= 1000):
        actual_memory_size = str(round(float(size) * 0.93, 2)) + 'GB'
    elif unit == 'MB' and size < 1000:
        actual_memory_size = str(int(float(size) * 0.93)) + 'MB'
    else:
        raise ValueError("Invalid memory size format. Use 'GB' or 'MB'.")
    
    return actual_memory_size

if __name__ == '__main__':
    func = actualMemorySize
    inputs = [
        '32GB',
        '2GB',
        '512MB',
        '1GB',
        '1000MB',
        '256MB',
        '128GB',
        '64GB',
        '16GB',
        '8GB',
        '4GB',
        '2MB',
        '1MB',
        '0.5GB',
        '0.25GB',
        '0.1GB',
        '0.01GB',
        '0.001GB',
        '0.0001GB',
        '0.00001GB',
        '0.000001GB',
        '0.0000001GB'
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
