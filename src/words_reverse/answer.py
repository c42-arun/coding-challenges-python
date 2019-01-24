import unittest

def reverse(list_of_chars, start, end):

        left_index = start
        right_index = end

        while left_index < right_index:
            # Swap characters
            # in-place without using a temp var!!
            list_of_chars[left_index], list_of_chars[right_index] = \
                list_of_chars[right_index], list_of_chars[left_index]

            # Move towards middle
            left_index += 1
            right_index -= 1

def reverse_words(message):

    # Decode the message by reversing the words
    
    # 1 - Reverse chars for entire msg
    reverse(message, 0, len(message) - 1)

    # 2 - Reverse chars for individual words
    
    # initialise
    word_start = 0
    '''
    for counter, letter in enumerate((message)):
        if (letter == ' ') :
            print(f'{message} {word_start} {counter}')
            reverse(message, word_start, counter - 1)

            word_start = counter + 1

    reverse(message, word_start, len(message) - 1)
    '''

    for i in range(len(message) + 1): # we want to go one over the last index
        if ((i == len(message)) or (message[i] == ' ')):
            print(f'{message} {word_start} {i}')
            reverse(message, word_start, i - 1)

            word_start = i + 1        

if __name__ == "__main__":
    pass
    msg = list('yummy is cake bundt chocolate')
    
    print(msg)

    reverse_words(msg)

    print(msg)



# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
