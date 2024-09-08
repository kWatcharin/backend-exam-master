import unittest
from ex1_find_tailing_zero.main import Solution as Sol1
from ex2_index_of_max.main import Solution as Sol2
from ex3_number_to_thai.main import Solution as Sol3
from ex4_number_to_roman.main import Solution as Sol4


class TestSolution(unittest.TestCase):
    
    def test_find_tailing_zero(self):
        print("Solution 1:", self._testMethodName)
        number: int = 15 # กำหนด ค่าตัวเลขสมมุติเท่ากับ 15! ซึ่งคำนวณ Factorial = 1307674368000.
        count_zeroes: int = 3 # จากการคำนวณ Factorial พบว่ามีเลข 0 ติดกัน 3 ตัว
        
        sol1 = Sol1()
        self.assertEqual(sol1.find_tailing_zeroes(number=number), count_zeroes)
    
    
    def test_find_max_index(self):
        print("Solution 2:", self._testMethodName)
        numbers: list = [1,2,1,3,5,6,4]
        max_value_index: int = 5 # จาก ตัวแปร numbers พบว่าเลข index ของค่าสูงสุดคือ 5
        
        sol2 = Sol2()
        self.assertEqual(sol2.find_max_index(numbers=numbers), max_value_index)
        
        
    def test_number_to_thai(self):
        print("Solution 3:", self._testMethodName)
        number: int = 123_459
        th_number_text: str = "หนึ่งแสนสองหมื่นสามพันสี่ร้อยห้าสิบเก้า"
        
        # สำหรับ เทส กรณีเลขเกินกว่าหรือเท่ากับ 10 ล้าน
        # number: str = 10_000_000
        # th_number_text: str = "สิบล้าน"
        
        sol3 = Sol3()
        self.assertEqual(sol3.number_to_thai(number=number), th_number_text)
        
        
    def test_number_to_roman(self):
        print("Solution 4:", self._testMethodName)
        arabic_number: int = 987
        roman_number: str = 'CMLXXXVII'
        
        sol4 = Sol4()
        self.assertEqual(sol4.number_to_roman(number=arabic_number), roman_number)
        
        
if __name__ == "__main__":
    unittest.main()