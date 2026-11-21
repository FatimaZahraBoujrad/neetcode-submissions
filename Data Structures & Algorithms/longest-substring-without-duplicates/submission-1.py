class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        sub=""
        characters=set()
        max_sub=0
        for r in range(len(s)):
            sub+=s[r]
            while s[r] in characters:
                sub=s[left+1:r+1]
                characters.remove(s[left])
                left+=1
            max_sub=max(max_sub,len(sub))
            characters.add(s[r])
        return max_sub
