import unittest

def reverse(list_of_chars):

        left_index = 0
        right_index = len(list_of_chars) - 1

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
    reverse(message)

    # 2 - Reverse chars for individual words
    
    # initialise
    word_start = 0
    a_word = []

    for counter, letter in enumerate(message):
        if (letter == ' '):
            reverse(a_word)

            word_index = 0
            for w in a_word:
                message[word_start + word_index] = w
                word_index += 1
            message[word_start + word_index] = letter

            word_start = counter + 1
            a_word = []
        else:
            a_word.append(letter)
        
        counter += 1

    reverse(a_word)
    word_index = 0
    for w in a_word:
        message[word_start + word_index] = w
        word_index += 1

# if __name__ == "__main__":
#     msg = list('ryummy is cake bundt chocolate')
    
#     # print(msg)

#     reverse_words(msg)

#     print(msg)



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
