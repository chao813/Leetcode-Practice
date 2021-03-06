"""Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?"""

def reverseBits(self, n):
        temp=bin(n)[2:]
  
        length=32-len(temp) 
        padding='{:032b}'.format(0)

        result=padding[:length]+temp

        return int(result[::-1],base=2)