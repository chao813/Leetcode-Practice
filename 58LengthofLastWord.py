"""Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip(' ')
        print(s)
        if s=="":
            return 0
        return len(s.split(' ')[-1])