def split_into_buckets(phrase: str, buckets: int) -> list[str]:
    '''Divides a phrase into word buckets where each bucket has ≤ n characters.
    
    Splits the input phrase into buckets (groups of words) where each bucket:
    - Contains only complete words
    - Has a total length (including spaces between words) ≤ the specified bucket size
    - Has no leading or trailing spaces
    
    If any word is longer than the bucket size, returns an empty list immediately.
    When words can't be grouped without exceeding the bucket size, returns them as individual buckets.

    Args:
        phrase: The input string to be bucketized. Can be empty.
        buckets: Maximum number of characters allowed per bucket (must be ≥ 0).

    Returns:
        A list of strings where each string is a valid bucket, or an empty list if:
        - Any word exceeds the bucket size
        - The input phrase is empty
        - Bucket size is 0 (unless phrase is also empty)
    '''
    words = phrase.split()
    answer = []
    current = ''
    for word in words:
        if len(word) > buckets:
            return []

        if not current:
            new_current = word
        else:
            new_current = current + ' ' + word

        if len(new_current) <= buckets:
            current = new_current
        else:
            answer.append(current)
            current = word

    if current:
        answer.append(current)

    return answer
    

if __name__ == '__main__':
    inputs = [("she sells sea shells by the sea", 10), ("the mouse jumped over the cheese", 7), ("fairy dust coated the air", 20), ("a b c d e", 2)]
    func = split_into_buckets
    for item in inputs:
        print(func(item[0], item[1]))
