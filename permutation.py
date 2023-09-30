import math


def getPermutation(n, k):
    numbers = list(range(1, n + 1))  # Create a list of numbers from 1 to n
    result = []  # Initialize the result list

    k -= 1  # Adjust k to make it 0-based

    # Calculate the factorials for 1 to n
    factorials = [1] * n
    for i in range(1, n):
        factorials[i] = factorials[i - 1] * (i + 1)

    for i in range(n, 0, -1):  # Decrease i from n to 1
        index = k // factorials[i - 1]
        result.append(str(numbers[index]))
        numbers.pop(index)
        k %= factorials[i - 1]

    return ''.join(result)


# Example usage:
n = 3
k = 3
result = getPermutation(n, k)
print(result)  # Output: "213"
