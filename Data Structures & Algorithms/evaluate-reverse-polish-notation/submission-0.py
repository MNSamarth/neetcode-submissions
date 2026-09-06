class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=0
        stack=[]
        oper=('+','-','*','/')
        for t in tokens:
            if t in oper:
                x=stack.pop()
                y=stack.pop()
                if t=='+':
                    result=(y+x)
                elif t=='-':
                    result=(y-x)
                elif t=='*':
                    result=(y*x)
                else:
                    result=int(y/x)
                stack.append(int(result))
            else:
                stack.append(int(t))
        return stack.pop()