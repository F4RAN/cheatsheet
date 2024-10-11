def isMatch(self, s: str, p: str) -> bool:
        cache = {}  # Memoization cache to store results of subproblems

        def dfs(i, j):
            # Check if the current state has already been computed
            """
            # Example:
            # Suppose we have previously computed dfs(1, 2) and stored the result as False
            cache = {(1, 2): False}
            # Calling dfs(1, 2) again will return False immediately without further computation
            """
            if (i, j) in cache:
                return cache[(i, j)]

            # If both the string and pattern have been fully matched
            """
            # Example:
            # s = "abc", p = "abc"
            # When i = 3 and j = 3 (both indices are at the end of their respective strings)
            # This condition is met, and the function returns True
            """
            if i >= len(s) and j >= len(p):
                return True

            # If the pattern is exhausted but the string is not
            """
            # Example:
            # s = "abcd", p = "abc"
            # When i = 3 and j = 3, the pattern is exhausted but the string has one more character 'd'
            # This condition is met, and the function returns False
            """
            if j >= len(p):
                cache[(i, j)] = False
                return False

            # Check if the current characters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            # Handle the '*' wildcard in the pattern
            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = (
                    dfs(i, j + 2) or  # Option 1: Skip '*' and preceding character
                    (match and dfs(i + 1, j))  # Option 2: Use '*' to match current character
                )
                return cache[(i, j)]

            # If current characters match, move to the next characters in both string and pattern
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            # If characters do not match and there's no '*' to handle it, it's not a match
            cache[(i, j)] = False
            return False

        return dfs(0, 0)
