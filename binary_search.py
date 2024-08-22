def binary_search(lst, item):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (high + low) // 2
        guess = lst[mid]
        if guess < item:
            low = mid + 1
        elif guess == item:
            return mid
        elif guess > item:
            high = mid - 1
    return None

my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))