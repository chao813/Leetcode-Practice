"""Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y"."""

 def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = ""
        temp = []
        t = []
        for i in s:
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                temp.append(i)
                t.append('*')        
            else:
                t.append(i)
        
        x = -1
        for n , letter in enumerate(t):
            if letter == "*":
                t[n] = temp[x]
                x = x - 1
        return("".join(t))