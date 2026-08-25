class Solution(object):
    def generateParenthesis(self, n):
        result = []
        brackets = []

        def solve(open_count, close_count):
            # If we have used all n pairs
            if open_count == n and close_count == n:
                result.append("".join(brackets))
                return

            # Add '(' if we still have some left
            if open_count < n:
                brackets.append("(")
                solve(open_count + 1, close_count)
                brackets.pop()

            # Add ')' only when it won't make the sequence invalid
            if close_count < open_count:
                brackets.append(")")
                solve(open_count, close_count + 1)
                brackets.pop()

        solve(0, 0)
        return result