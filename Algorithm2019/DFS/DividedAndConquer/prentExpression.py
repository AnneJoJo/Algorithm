# ['F', '|', 'T', '&', 'T']

def addParentheses(expression):
    """

    :param expression: array
    :return:
    """
    ret = [0]*len(expression)

    for i, v in enumerate(expression):
        if len(expression) == 1:
            return expression[0]

        if v in ['&','|','^']:
            left = addParentheses(expression[:i])
            right = addParentheses(expression[i+1:])
            if v == '&':
                res = left and right
            elif v == '|':
                res = left or right
            elif v == '^':
                res = left ^ right

            ret[i] = res
        print (ret)
    return res




addParentheses([False,'&',True, '&',True])


