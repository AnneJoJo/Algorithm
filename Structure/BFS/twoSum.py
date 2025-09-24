from cmath import inf
from collections import Counter, defaultdict
def sliding_window(s, target):
    targetCounter = Counter(target)  # 要求字符频率
    windowCounter = defaultdict(int)  # 当前窗口字符频率
    
    left = 0
    right = 0
    minLen = inf
    result = ""  # 可选

    while right < len(s):
        windowCounter[s[right]] += 1

        # 收缩窗口
        while is_window_valid(targetCounter, windowCounter):
            # 更新答案（按需求记录结果）
            minLen = min(minLen, right - left + 1)
            result = s[left:right+1]  # 可选

            windowCounter[s[left]] -= 1
            left += 1

        right += 1

    return result or minLen
def is_window_valid(target, window):
    for key in target:
        if window[key] < target[key]:
            return False
    return True


from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()  # store indices
    result = []

    for right in range(len(nums)):
        # 1. 维护递减顺序：把比当前 nums[right] 小的元素从队尾弹出
        while dq and nums[dq[-1]] < nums[right]:
            dq.pop()

        # 2. 加入当前 index
        dq.append(right)

        # 3. 检查队首是否过期（是否已经滑出窗口左边）
        if dq[0] < right - k + 1:
            dq.popleft()

        # 4. 如果窗口已经满，记录当前最大值
        if right >= k - 1:
            result.append(nums[dq[0]])

    return result
