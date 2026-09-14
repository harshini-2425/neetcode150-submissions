class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longeststreak = 0
        for num in numset:
            if (num-1) not in numset:
                currentnum = num
                currentstreak = 1
                while (currentnum+1) in numset:
                    currentnum += 1
                    currentstreak += 1
                longeststreak = max(longeststreak,currentstreak)     
        return longeststreak