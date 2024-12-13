# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1
 

# Follow up: Could you solve it without converting the integer to a string?




class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        num = x
        if num < 0 or (num % 10 == 0 and num != 0):
            return False
    
        reverse = 0
        original = num  # Store the original number for final comparison
    
        while num > 0:
            digit = num % 10  # Get the last digit
            reverse = reverse * 10 + digit  # Build the reversed number
            num //= 10  # Remove the last digit
    
        return original == reverse  # Compare the original number with its reverse