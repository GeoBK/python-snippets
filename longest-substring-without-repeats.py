class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        curr_str=""
        for i in s:
            if i in curr_str:
                index=curr_str.index(i)
                curr_str=curr_str[index+1:]            
            curr_str=curr_str+i

sol= Solution()
sol.lengthOfLongestSubstring("HelloWorld!")