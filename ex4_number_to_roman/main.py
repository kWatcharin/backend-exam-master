"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""

_DIGIT_4 = ['', 'M']
_DIGIT_3 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
_DIGIT_2 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
_DIGIT_1 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

class Solution:

    def number_to_roman(self, number: int) -> str:
        match number:
            case number if number < 0:
                raise ValueError("Number can not be less than 0!")
            case number if number > 1000:
                raise ValueError("Number can not greater than 1000!")
            case _:
                digit_4: str = _DIGIT_4[number//1000]
                digit_3: str = _DIGIT_3[(number%1000)//100]
                digit_2: str = _DIGIT_2[(number%100)//10]
                digit_1: str = _DIGIT_1[(number%10)//1]
                roman_number: str = digit_4 + digit_3 + digit_2 + digit_1
                
                return roman_number
