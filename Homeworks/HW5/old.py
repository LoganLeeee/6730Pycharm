def max_relative_frequency(s):
    # import string # No need of this in new method.
    # In case there are some upper letters.
    s = s.lower()
    length_of_letter = 0
    highest_relative_frequency = 0
    '''
    for i in range(len(s)):
        # Count Only letters of the English alphabet,no other languages
        # import string needed for the function ASCII
        if s[i] in string.ascii_letters:
            length_of_letter = length_of_letter + 1
     # No need of this in new method.
    '''
    for i in range(97, 123):
        # Count letter appeared times ONLY from a to z and add to length.
        length_of_letter = length_of_letter + s.count(chr(i))
        # Find highest relative frequency
        if s.count(chr(i)) > highest_relative_frequency:
            highest_relative_frequency = s.count(chr(i))
    # In case input string is empty
    if length_of_letter == 0:
        return 0
    else:
        return highest_relative_frequency / length_of_letter