from collections import deque

def removeInvalidParentheses(s):
    """
    :type s: str
    :rtype: List[str]
    """
    def is_valid(ss):
        count = 0
        for c in ss:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
            if count < 0:
                return False
        return count == 0

    visited = set()
    queue = deque()
    result = []
    queue.append(s)
    visited.add(s)
    found_valid = False

    while queue:
        level_size = len(queue)
        for _ in range(level_size):
            current = queue.popleft()
            if is_valid(current):
                result.append(current)
                found_valid = True  # Mark to collect all at this level
            # Skip generating next level if valid found
            if found_valid:
                continue
            # Generate all possible next states
            for i in range(len(current)):
                if current[i] not in '()':
                    continue  # Skip non-parentheses
                next_str = current[:i] + current[i+1:]
                if next_str not in visited:
                    visited.add(next_str)
                    queue.append(next_str)
        # Stop after processing the current level
        if found_valid:
            break

    return result if result else ['']