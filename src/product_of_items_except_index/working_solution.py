import unittest

# returns product of all items in the list beginning at 'fromIndex'
def get_all_products(L, fromIndex):
    product = 1
    for i in range(fromIndex, len(L)):
        product = product * L[i]

    return product

def get_product_of_integers_before_index(L):
    product_of_integers_before_index = []
    productSoFar = 1

    for i in range(len(L)):
        product_of_integers_before_index.append(productSoFar)
        productSoFar = productSoFar * L[i]

    return product_of_integers_before_index


def get_product_of_integers_after_index(L, beforeIndexProducts):
    # product_of_integers_after_index = []
    productSoFar = 1

    for i in range(len(L)-1, -1, -1):
        print(f"{productSoFar} x {beforeIndexProducts[i]}")
        beforeIndexProducts[i] = productSoFar * beforeIndexProducts[i]
        productSoFar = productSoFar * L[i]

    # product_of_integers_after_index.reverse()

    return beforeIndexProducts


def get_products_of_all_ints_except_at_index(int_list):
    # int_list = [4, 5, 8, 6, 7] 
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                        'indices requires at least 2 numbers')

    # result should be [1, 4, 20, 160, 720]
    listWithBeforeIndexProducts = get_product_of_integers_before_index(int_list)
    print(listWithBeforeIndexProducts)

    # result should be [1680, 336, 42, 7, 1]
    listWithBeforeAndAfterProducts = get_product_of_integers_after_index(int_list, listWithBeforeIndexProducts)
    print(listWithBeforeAndAfterProducts)    

    return listWithBeforeAndAfterProducts


class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)  