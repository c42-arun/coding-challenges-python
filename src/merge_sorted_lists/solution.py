import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    
    result = [0] * (len(my_list) + len(alices_list))

    my_index = 0
    alice_index = 0

    for i in range(len(result)):
        # if my_index is exhausted, take values from alices_list
        if (my_index >= len(my_list)):
            result[i] = alices_list[alice_index]
            alice_index += 1
        
        # if alices_list is exhausted, take values from my_index
        elif (alice_index >= len(alices_list)):
            result[i] = my_list[my_index]
            my_index += 1

        # if my_list[my_index] is less than alices_list[alice_index],
        #   take my_list[my_index] & increment my_index
        elif (my_list[my_index] < alices_list[alice_index]):
            result[i] = my_list[my_index]
            my_index += 1

        # if alices_list[alice_index] is less than my_list[my_index],
        #   take alices_list[alice_index] & increment alice_index
        elif (my_list[my_index] > alices_list[alice_index]):
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