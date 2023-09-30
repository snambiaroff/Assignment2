def largestRectangleArea(heights):
    stack = []  # Initialize a stack to store the indices of the histogram bars
    max_area = 0  # Initialize the maximum area

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        stack.append(i)

    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        max_area = max(max_area, height * width)

    return max_area


heights = [3, 2, 4, 5, 7, 6, 1, 3, 8, 10, 11, 10, 7, 5, 2, 6]
result = largestRectangleArea(heights)
print(result)  
