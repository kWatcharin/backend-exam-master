"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""

class Solution:
    
    def _find_factorial(self, number: int) -> int:
        match number:
            case number if number < 0:
                raise ValueError("Number can not be negaive!")
            case number if number == 0 | number == 1:
                return 1
            case _:
                return number * self._find_factorial(number = number - 1)
    
    
    def find_tailing_zeroes(self, number: int) -> int | str:
        factorial: int = self._find_factorial(number=number)
        count: int = 0
        
        while factorial % 10 == 0:
            count += 1
            factorial //= 10
            
        return count