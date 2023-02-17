# Leet code problem
# Given a roman numeral string, convert it to an integer

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def romanToInt(self, s: str) -> int:

        # Initialize integer at 0
        sol = 0

        # Loop over every element of string
        for i in range(len(s)):

            # Add 1000 for M
            if (s[i] == 'M'):
                sol = sol + 1000

            # Add 500 for D
            elif (s[i] == 'D'):
                sol = sol + 500

            # Add 100 for C, but subtract if before D or M
            elif (s[i] == 'C'):
                if (i != len(s)-1) and ((s[i+1] == 'D') or (s[i+1] == 'M')):
                    sol = sol - 100
                else:
                    sol = sol + 100

            # Add 50 for L
            elif (s[i] == 'L'):
                sol = sol + 50

            # Add 10 for X, but subtract if before L or C
            elif (s[i] == 'X'):
                if (i != len(s)-1) and ((s[i+1] == 'L') or (s[i+1] == 'C')):
                    sol = sol - 10
                else:
                    sol = sol + 10

            # Add 5 for V
            elif (s[i] == 'V'):
                sol = sol + 5

            # Add 1 for I, but subtract if before V or X
            else:
                if (i != len(s)-1) and ((s[i+1] == 'V') or (s[i+1] == 'X')):
                    sol = sol - 1
                else:
                    sol = sol + 1
        return sol

# Test example
s = 'MCMXCIV'
print(Solution().romanToInt(s))