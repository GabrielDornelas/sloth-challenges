from math import factorial

def fact_of_fact(num: int) -> int:
    '''
    This function that takes an integer n and returns the factorial of factorials. See below examples for a better understanding:

    Examples
    fact_of_fact(4)
    output = 288
    // 4! * 3! * 2! * 1! = 288

    fact_of_fact(5)
    output = 34560

    fact_of_fact(6)
    output = 24883200

    Args:
        num: The input integer to calculate.

    Returns:
        int: Factorial of factorials.
    '''
    total = 1
    all = list(range(1, num + 1))
    for item in all:
        total *= factorial(item)
    return total

if __name__ == '__main__':
    func = fact_of_fact
    inputs = [
        4,
        5,
        6
    ]
    for item in inputs:
        print(f"{item}: {func(item)}")
