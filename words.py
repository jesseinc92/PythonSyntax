def print_upper_words(words, must_start_with):
    '''Accepts two parameters:

        - a list of words
        - specific letters

    For a list of words, print each out only the words beginning with the specified letters in all uppercase.'''

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break