"""
เขียนโปรแกรมหา index ของตัวเลขที่มีค่ามากที่สุดใน list

[Input]
numbers: list of numbers

[Output]
index: index of maximum number in list

[Example 1]
input = [1,2,1,3,5,6,4]
output = 5

[Example 2]
input = []
output = list can not blank
"""


class Solution:
    
    def find_max_index(self, numbers: list) -> int | str:
        match numbers:
            case []:
                raise ValueError("List can not blank!")
            case _:
                max_value: int = max(numbers)
                max_value_index: int = numbers.index(max_value)
        
                return max_value_index
