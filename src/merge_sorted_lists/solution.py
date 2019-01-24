import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    
    result = [0] * (len(my_list) + len(alices_list))

    my_index = 0
    alice_index = 0

    for i in range(len(result)):
        mine_exhausted = my_index >= len(my_list)
        alice_exhausted = alice_index >= len(alices_list)

        # Next comes from Mine if
        #   1. Mine is not exhausted AND
        #       2. Alice is exhausted OR
        #       3. Mine's is smaller than Alice's
        if (not mine_exhausted and 
                (alice_exhausted or my_list[my_index] < alices_list[alice_index])):
            result[i] = my_list[my_index]
            my_index += 1
        
        # else comes from my Alice
        else:
            result[i] = alices_list[alice_index]
            alice_index += 1

    return result
    


if __name__ == "__main__":
    pass
    l1 = [2, 4, 6]
    l2 = [1, 3, 7]
    result = merge_lists(l1, l2)
    print(result)


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)