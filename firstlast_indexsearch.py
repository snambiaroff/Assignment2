def find_first_last_position(arr, target):
    low, high = 0, len(arr) - 1
    first_position, last_position = -1, -1

    # we use Binary search in this program
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first_position = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # setting low and high pointers
    low, high = 0, len(arr) - 1

    # Binary search for the last position
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last_position = mid
            low = mid + 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return [first_position, last_position]


arr = [1, 2, 2, 2, 3, 4, 5, 5, 5, 6]
target = 5
result = find_first_last_position(arr, target)
print(result)
