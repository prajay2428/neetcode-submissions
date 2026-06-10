class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = { '+': lambda x,y : x+y,
                      '-': lambda x,y : x-y,
                      '*': lambda x,y : x*y,
                      '/': lambda x,y : x/y
        }
        stk=[]

        for op in tokens:
            print(stk)
            if op not in operators:
                stk.append(op)
            else:
                op1=stk.pop(-1)
                op2=stk.pop(-1)
                result =operators[op](int(op2),int(op1))
                stk.append(result)

        return int(stk[-1])


        