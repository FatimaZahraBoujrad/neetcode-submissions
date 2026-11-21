class Solution:
    def isValid(self, s: str) -> bool:
        para={')':'(','}':'{',']':'['}
        openp=set(para.values())
        stack=[]
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i] in openp:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                right=stack.pop()
                if right!=para[s[i]]:
                    return False
            
        return False if len(stack)!=0  else True