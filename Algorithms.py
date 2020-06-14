def binary_search(my_list, item):
    """This algorithm find items quickly than others"""
    low = 0
    high = len(my_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = my_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None
