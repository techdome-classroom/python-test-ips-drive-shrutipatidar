def longest_substring(s: str) -> int:
    # Call the provided longest_substring function to find the length of the longest substring without repeating characters
    def longest_substring_without_repeating(s):
        char_index = {}
        max_length = 0
        start = 0

        for end in range(len(s)):
            if s[end] in char_index and char_index[s[end]] >= start:
                start = char_index[s[end]] + 1

            char_index[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length

    # Call the helper function and return its result
    
    return longest_substring_without_repeating(s)




