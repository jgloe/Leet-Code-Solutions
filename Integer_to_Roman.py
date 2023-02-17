# Leet code problem
# Given an integer, return its equivalent in roman numerals

class Solution:

    def __init__(self):
        self.name = 'Solution'

    def intToRoman(self, num: int) -> str:

        # Initialize hash table with roman numerals
        rom = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX',
        10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC',
        100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC',
        900:'CM', 1000:'M', 2000:'MM', 3000:'MMM'}

        # Initialize output string
        rom_str = ''

        # Compute ones, tens, hundreds, and thousands place
        ones = num % 10
        tens = (num % 100) - ones
        hundreds = (num % 1000) - tens - ones
        thousands = num - hundreds - tens - ones

        # Create output string
        if (ones != 0):
            rom_str = rom[ones] + rom_str
        if (tens != 0):
            rom_str = rom[tens] + rom_str
        if (hundreds != 0):
            rom_str = rom[hundreds] + rom_str
        if (thousands != 0):
            rom_str = rom[thousands] + rom_str
        return rom_str

# Example to test    
num = 3164
print(Solution().intToRoman(num))