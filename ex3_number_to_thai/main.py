"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""

_DIGIT_7 = ['', 'หนึ่งล้าน', 'สองล้าน', 'สามล้าน', 'สี่ล้าน', 'ห้าล้าน', 'หกล้าน', 'เจ็ดล้าน', 'แปดล้าน', 'เก้าล้าน']
_DIGIT_6 = ['', 'หนึ่งแสน', 'สองแสน', 'สามแสน', 'สี่แสน', 'ห้าแสน', 'หกแสน', 'เจ็ดแสน', 'แปดแสน', 'เก้าแสน']
_DIGIT_5 = ['', 'หนึ่งหมื่น', 'สองหมื่น', 'สามหมื่น', 'สี่หมื่น', 'ห้าหมื่น', 'หกหมื่น', 'เจ็ดหมื่น', 'แปดหมื่น', 'เก้าหมื่น']
_DIGIT_4 = ['', 'หนึ่งพัน', 'สองพัน', 'สามพัน', 'สี่พัน', 'ห้าพัน', 'หกพัน', 'เจ็ดพัน', 'แปดพัน', 'เก้าพัน']
_DIGIT_3 = ['', 'หนึ่งร้อย', 'สองร้อย', 'สามร้อย', 'สี่ร้อย', 'ห้าร้อย', 'หกร้อย', 'เจ็ดร้อย', 'แปดร้อย', 'เก้าร้อย']
_DIGIT_2 = ['', 'สิบ', 'ยี่สิบ', 'สามสิบ', 'สี่สิบ', 'ห้าสิบ', 'หกสิบ', 'เจ็ดสิบ', 'แปดสิบ', 'เก้าสิบ']
_DIGIT_1 = ['', 'เอ็ด', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']


class Solution:

    def number_to_thai(self, number: int) -> str:
        match number:
            case number if number >= 10_000_000:
                raise ValueError("Number equal to 10,000,000 or greater than!")
            case number if number < 0:
                raise ValueError("Number can not less than 0!")
            case 1:
                return "หนึ่ง"
            case 0:
                return "ศูนย์"
            case _:
                digit_7: str = _DIGIT_7[number//1000000]
                digit_6: str = _DIGIT_6[(number%1000000)//100000]
                digit_5: str = _DIGIT_5[(number%100000)//10000]
                digit_4: str = _DIGIT_4[(number%10000)//1000]
                digit_3: str = _DIGIT_3[(number%1000)//100]
                digit_2: str = _DIGIT_2[(number%100)//10]
                digit_1: str = _DIGIT_1[(number%10)//1]
                th_text_number: str = digit_7 + digit_6 + digit_5 + digit_4 + digit_3 + digit_2 + digit_1
                
                return th_text_number
