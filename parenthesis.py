def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            combinations.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    combinations = []
    backtrack('', 0, 0)
    return combinations


n = 3
result = generate_parentheses(n)
print(result)
