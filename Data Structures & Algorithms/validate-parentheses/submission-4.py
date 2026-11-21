class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        valid=deque()
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for c in s:
            if c in closeToOpen.values():
                valid.append(c)
          
            else:
                if len(valid)==0:
                    return False
                opn=valid.pop()
                if opn!=closeToOpen[c]:
                    return False
        return len(valid)==0






























