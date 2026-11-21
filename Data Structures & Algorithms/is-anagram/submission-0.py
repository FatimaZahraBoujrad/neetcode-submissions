class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        occ_s={}
        occ_t={}
        for i in range(len(s)):
            if s[i] in occ_s:
                occ_s[s[i]]+=1
            else:
                occ_s[s[i]]=1
            if t[i] in occ_t:
                occ_t[t[i]]+=1
            else:
                occ_t[t[i]]=1

        for key,value in occ_s.items():
            if key not in occ_t or occ_t[key]!=value:
                return False
        return True