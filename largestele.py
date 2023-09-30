import random


def quick_select(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot element
    pivot = random.choice(arr)

    # Partition the array into three parts: elements less than, equal to, and greater than the pivot
    less_than_pivot = [x for x in arr if x < pivot]
    equal_to_pivot = [x for x in arr if x == pivot]
    greater_than_pivot = [x for x in arr if x > pivot]

    # Determine which partition to recursively search
    if k <= len(greater_than_pivot):
        return quick_select(greater_than_pivot, k)
    elif k <= len(greater_than_pivot) + len(equal_to_pivot):
        return pivot
    else:
        return quick_select(less_than_pivot, k - len(greater_than_pivot) - len(equal_to_pivot))


arr = [3, 1, 4, 2, 5]
k = 2
result = quick_select(arr, k)
print(result)
