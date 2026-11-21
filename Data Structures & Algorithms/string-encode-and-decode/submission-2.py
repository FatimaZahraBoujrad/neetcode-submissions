class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str=""
        for s in strs:
            final_str=final_str+str(len(s))+"#"+s
        return final_str

    def decode(self, s: str) -> List[str]:
        i=0
        
        strs=[]
        while i<len(s):
            j=s.index("#",i)
            len_str=int(s[i:j])
            strs.append(s[j+1:j+len_str+1])
            i=j+len_str+1
      
        return strs