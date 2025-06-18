def birthdayCakeCandles(candles: list[int]) -> int:
    '''
    This function will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles.
    The task is to count how many candles are the tallest.

    Examples
    birthdayCakeCandles([4,4,1,3])
    output = 2
    // The tallest candles are 4. There are 2 candles with this height, so the function should return 2.
    birthdayCakeCandles([1, 1, 1, 1])
    output = 4
    // All candles are the same height, so all are the tallest.
    birthdayCakeCandles([])
    output = 0
    // No candles, so nothing to blow out.

    Args:
        candles: The input list of integer of candles.

    Returns:
        int: SUM of total tallest candles.
    '''
    return 0 if (not candles or max(candles) == 0) else candles.count(max(candles))

if __name__ == '__main__':
    func = birthdayCakeCandles
    inputs = [
        [4,4,1,3],
        [1, 1, 1, 1],
        [],
        [3, 2, 1, 3],
        [5, 5, 5, 5, 5],
        [1, 2, 3, 4, 5],
        [10, 20, 30, 40],
        [7],
        [2, 2, 2],
        [6, 6, 6, 6],
        [3, 3],
        [1],
        [0]
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
