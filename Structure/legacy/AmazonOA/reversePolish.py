def evalRPN(self, tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    q=[]
    for s in tokens:
        if s in "+-*/":
            b=q.pop()
            a=q.pop()
            if s=="+" :
                q.append(a+b) 
            if s=="-" : 
                q.append(a-b) 
            if s=="*" : 
                q.append(a*b)
            if s=="/" : 
                q.append(int(operator.truediv(a, b)))
        else:
            q.append(int(s))
    return (q[0])