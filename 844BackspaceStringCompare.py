"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b"."""


def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        
        
        t1 = ""
        for i in S:
            if i == '#':
                t1 = t1[:-1]
            else:
                t1 += i
        
        t2 = ""
        for i in T:
            if i == '#':
                t2 = t2[:-1]
            else:
                t2 += i
       
        
        return t2 == t1