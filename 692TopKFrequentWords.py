"""Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space."""


def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        ans = []
        dic = {}
        for word in words:
            if word not in dic.keys():
                dic[word] = 1
            else:
                dic[word] += 1
        
        print(dic)
        s = [(kk, dic[kk]) for kk in sorted(dic, key=dic.get, reverse=True)]
        for key, value in s:
            ans.append(key)
        print(ans)
        return ans[0:k]
    
    
    
        """from collections import Counter
        dic = Counter(words)
        for i,w in enumerate(words):
            words[i] = (dic[w],w)
        words = list(set(words))
        words = sorted(words,key = lambda x: x[1])
        words = sorted(words,key = lambda x: x[0],reverse = True)
        return [words[i][1] for i in range(k)]"""