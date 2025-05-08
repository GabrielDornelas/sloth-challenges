def isShuffledWell(array: list[int]) -> bool:
    '''Check if given array has a sequence equal or greater than 3 sequential numbers.
    A sequence is considered either ascending or descending (e.g., 1,2,3 or 4,3,2 or 1,2,1).

    Args:
        array: The input list of ints from 1 to 10.

    Returns:
        bool: True if the array is well shuffled (no sequences of 3+ numbers), 
              False if it contains such sequences.
    '''
    prev = -1
    sequence = 1
    for i in range(1, len(array)):
        prev = array[i - 1]
        current = array[i]
        if abs(current - prev) == 1:
            sequence += 1
            if sequence >= 3:
                return False
        else:
            sequence = 1
    return True
    

if __name__ == '__main__':
    inputs = [
        [1, 2, 3, 5, 8, 6, 9, 10, 7, 4],
        [3, 5, 1, 9, 8, 7, 6, 4, 2, 10],
        [1, 5, 3, 8, 10, 2, 7, 6, 4, 9],
        [1, 3, 5, 7, 9, 2, 4, 6, 8, 10],
        [5, 6, 7, 1, 2, 3],
        [10, 9, 8, 1, 2, 3],
        [1, 2, 4, 3, 2],
        [1, 2],
        [1, 2, 1]
    ]
    func = isShuffledWell
    for item in inputs:
        print(func(item))
