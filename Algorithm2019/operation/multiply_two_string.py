# regular solution
# vital part is to find right postion

def multi_string(num1,num2):
    if num1 == "" or num2 == "":
        return ""
    if num1 == '0' or num2 =='0':
        return "0"
    l1 = len(num1)
    l2 = len(num2)
    if l1 < l2:
        return multi_string(num2,num1)
    total_len = l1 + l2
    pos = total_len - 1
    res = [0]*total_len
    for i in range(len(num2))[::-1]:
        cur_pos = pos
        carry_bit = 0
        for j in range(len(num1))[::-1]:

            cur_total = int(num2[i])*int(num1[j]) + carry_bit + res[cur_pos]
            res[cur_pos] = cur_total % 10
            carry_bit = cur_total // 10
            cur_pos -= 1
        if carry_bit != 0:
            res[cur_pos] += carry_bit
        pos -= 1

    return ''.join(str(i) for i in res)

    for i in range(len(res)):
        if res[i] != 0:
            res = res[i:]
            break
print(multi_string('723','456'))


