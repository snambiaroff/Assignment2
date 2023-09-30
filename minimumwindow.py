from collections import Counter


def min_window(s, t):
    # Initialize a dictionary to store character frequencies in t
    t_counter = Counter(t)

    # Initialize variables for the sliding window
    left = 0
    min_len = float('inf')
    min_window_str = ""
    t_len = len(t)
    chars_to_match = t_len

    for right in range(len(s)):
        # Check if the current character is in t
        if s[right] in t_counter:
            t_counter[s[right]] -= 1
            if t_counter[s[right]] >= 0:
                chars_to_match -= 1

        # If all characters in t are matched, try to minimize the window
        while chars_to_match == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window_str = s[left:right+1]

            if s[left] in t_counter:
                t_counter[s[left]] += 1
                if t_counter[s[left]] > 0:
                    chars_to_match += 1

            left += 1

    return min_window_str


s = "ADCFEBECEABEBADFCDFCBFCBFCBEAD"
t = "ABCA"
result = min_window(s, t)
print(result)
