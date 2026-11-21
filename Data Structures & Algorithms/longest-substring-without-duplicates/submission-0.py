class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        max_sub=0
        sub=""
        count=Counter(sub)
        for r in range(len(s)):
            sub+=s[r]
            count[s[r]]+=1
            while count[s[r]]>1:
                
                sub=s[left+1:r+1]
                count[s[left]]-=1
                if count[s[left]]==0:
                    del count[s[left]]
                left+=1
            max_sub=max(len(sub),max_sub)
        return max_sub

            
