from collections import defaultdict, deque


def can_finish_courses(num_courses, prerequisites):
    # Create a graph representation using adjacency lists.
    graph = defaultdict(list)
    in_degree = [0] * num_courses

    # Build the graph and calculate in-degrees.
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1

    # Initialize a queue with courses that have no prerequisites.
    queue = deque()
    for course in range(num_courses):
        if in_degree[course] == 0:
            queue.append(course)

    # Perform topological sorting.
    while queue:
        course = queue.popleft()
        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If all courses have been taken (in-degree is 0), return True; otherwise, return False.
    return all(in_degree[i] == 0 for i in range(num_courses))


n = 6
prerequisites = [[0, 1], [3, 0], [1, 3], [
    2, 1], [4, 1], [4, 2], [5, 3], [5, 4]]
result = can_finish_courses(n, prerequisites)
print(result)
