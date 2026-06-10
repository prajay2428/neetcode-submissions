class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(',
        '}':'{',
        ']':'['}

        stack=[]

        for c in s:
            if c not in hashmap:
                stack.append(c)
            else :
                if len(stack) == 0:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[c]:
                        return False
        if len(stack) ==0:
            return True
        else:
            return False
        
        