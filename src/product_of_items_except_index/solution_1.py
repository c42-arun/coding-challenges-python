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


if __name__ == "__main__":
    int_list = [4, 5, 8, 6, 7] 
    
    # result should be [1, 4, 20, 160, 720]
    listWithBeforeIndexProducts = get_product_of_integers_before_index(int_list)
    print(listWithBeforeIndexProducts)

    # result should be [1680, 336, 42, 7, 1]
    listWithBeforeAndAfterProducts = get_product_of_integers_after_index(int_list, listWithBeforeIndexProducts)
    print(listWithBeforeAndAfterProducts)    