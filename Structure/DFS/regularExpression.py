# class Solution(object):
#     def isMatch(self, text: str, pattern: str) -> bool:
#         if not pattern:
#             return not text
#
#         first_match = bool(text) and pattern[0] in {text[0], "."}
#
#         if len(pattern) >= 2 and pattern[1] == "*":
#             return (
#                 self.isMatch(text, pattern[2:])
#                 or first_match
#                 and self.isMatch(text[1:], pattern)
#             )
#
#         else:
#             return first_match and self.isMatch(text[1:], pattern[1:])



    # 改进版本：保留你原本的结构 + 修复语法细节

def isValid(part):
    # 修复拼写错误：isStartWith → startswith
    return False if len(part) > 1 and part.startswith('0') else True

def addOperator(nums, target):
    res = []
    op = ['+', '-', '*']

    def backTrack(path, index):
        # 如果走到了末尾，把表达式加入结果
        if index == len(nums):
            res.append(path)
            return

        for i in range(index + 1, len(nums) + 1):  # 注意要 +1 才包含 i 位置,边界处理
            part = nums[index:i]
            print('parts', part)
            if not isValid(part):
                continue

            if index == 0:
                # 第一个数字前不能加运算符
                backTrack(part, i)
            else:
                for k in op:
                    backTrack(path + k + part, i)

    backTrack("", 0)
    return res

# 示例调用（暂不判断 target）
print(addOperator("123", 6))





#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"] 123   1 + 2+3




