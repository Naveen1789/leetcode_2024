'''
9. Palindrome Number

Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
'''

class Solution:
    def find_num_of_digits(self, x: int) -> int:
        num_of_digits = 0
        while (x > 0):
            x = x // 10
            num_of_digits = num_of_digits + 1
        return num_of_digits

    def isPalindrome(self, x: int) -> bool:
        # 1. Convert to string and reverse the string and compare with the original string
        # return str(x) == str(x)[::-1]

        # temp = x
        # if (temp < 0):
        #     return False

        # 2. Calculate the reverse number (without converting to string) - sub optimal
        # power_of_ten = self.find_num_of_digits(temp) - 1
        # inverted_number = 0
        # while (temp > 0):
        #     inverted_number = inverted_number + ((temp%10) * (10 ** power_of_ten))
        #     power_of_ten = power_of_ten - 1
        #     temp = temp//10

        # return x == inverted_number

        # 3. Calculate the reverse number (without converting to string) - optimal
        if (x < 0):
            return False

        temp = x
        rev_x = 0
        while temp > 0:
            last_digit = temp % 10
            rev_x = (rev_x * 10) + last_digit
            temp = temp // 10

        return x == rev_x
