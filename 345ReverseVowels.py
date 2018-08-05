"""Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y"."""

def reverseVowels(s):
	vowel = ['a','e','i','o','u']
    vowel_lst = []
    index_lst = []
    s = list(s)
    for i in range(len(s)):
        if s[i].lower() in vowel:
            vowel_lst.append(s[i])
            index_lst.append(i)
    vowel_lst = vowel_lst[::-1]
    
    for i,v in zip(index_lst,vowel_lst):
        s[i] = v
    return ''.join(s)


   