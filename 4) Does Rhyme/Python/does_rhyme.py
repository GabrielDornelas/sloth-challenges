import pronouncing

def get_formatted_word(word):
    """Remove pontuação e converte a palavra para minúsculas."""
    word = ''.join(char for char in word if char.isalnum())
    return word.lower()


def does_rhyme(first, second):
    '''
    Check if two statements rhyme using phonetic pronunciation.
    
    Args:
        first (str): The first input sentence.
        second (str): The second input sentence.
        
    Returns:
        bool: True if rhymes else False.
    '''
    first_list = first.split()
    first_last_word = get_formatted_word(first_list[-1])

    second_list = second.split()
    second_last_word = get_formatted_word(second_list[-1])

    # Get all the pronunciations of the last word
    first_pronunciations = pronouncing.rhymes(first_last_word)
    second_pronunciations = pronouncing.rhymes(second_last_word)

    # Two words rhyme if one is on the rhyming list of the other
    result = first_last_word in second_pronunciations or second_last_word in first_pronunciations

    print(f'First statement: {first}\nSecond statement: {second}')
    print(f'Checking phonetic rhymes: {first_last_word} vs {second_last_word} -> {result}')
    
    return result


if __name__ == '__main__':
    does_rhyme("Sam I am!", "Green eggs and ham.")
    does_rhyme("Sam I am!", "Green eggs and HAM.")
    does_rhyme("You're built like a seat", "I bet you like to eat")
    does_rhyme("You are off to the races", "a splendid day.")
    does_rhyme("and frequently do?", "you gotta move.")
