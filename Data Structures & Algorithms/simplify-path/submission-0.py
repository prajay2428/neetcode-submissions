class Solution:
    def simplifyPath(self, path: str) -> str:
        a = path.split("/")
        print(a)
        stk=[]

        for token in a:
            if token == "" or token ==".":
                continue
            
            if token == "..":
                if stk:
                    stk.pop()
                    
            else:
                stk.append(token)

        return "/" + "/".join(stk)
        
        

        