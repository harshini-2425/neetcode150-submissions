class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for num in s:
            freq1[num] = freq1.get(num,0)+1
        for num in t:
            freq2[num] = freq2.get(num,0)+1
        return freq1 == freq2
        