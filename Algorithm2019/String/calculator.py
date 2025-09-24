def evaluate_expr(s):
    stack = []
    num = 0
    sign = '+'

    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)

        if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                prev = stack.pop()
                # 向 0 取整的除法
                stack.append(int(prev / float(num)))
            # 更新当前运算符和数字
            sign = ch
            num = 0

    return sum(stack)
