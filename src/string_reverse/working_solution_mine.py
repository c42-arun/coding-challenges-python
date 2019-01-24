def reverse_string(char_list):
    # Idea is swap each ends and progrssively move to the centre
    # With odd length lists we leave the element in the centre
    # So we loop only half the length of the list - n/2 for even length list; (n-1)/2 for odd

    # if (len(char_list) < 2) return None

    list_len = len(char_list)
    upper_bound = list_len // 2 if list_len % 2 == 0 else (list_len - 1) // 2

    left = 0
    right = -1

    for i in range(0, upper_bound):
        temp = char_list[left]
        char_list[left] = char_list[right]
        char_list[right] = temp

        left += 1
        right -= 1
    
if __name__ == "__main__":
    str_list = list("do")

    print(str_list)

    reverse_string(str_list)

    print(str_list)


