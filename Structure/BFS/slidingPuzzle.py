class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        position = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[1,3,5],5:[2,4]} # neighbors to go
        queue = [self.flat_array(board)]
        seen = set()
        step = 0
        def find_zero(cur_p):
            for i in range(len(cur_p)):
                if(cur_p[i]=='0'):
                    return i
            return i-1


        while queue:
            for i in range(len(queue)):
                cur_pattern = queue.pop(0)
                if cur_pattern == '123450':
                    return step
                pos_zero = find_zero(cur_pattern)
                for pos_nei in position[pos_zero]:

                    temp_array = list(cur_pattern)

                    temp_array[pos_zero],temp_array[pos_nei] = temp_array[pos_nei],temp_array[pos_zero]
                    new_pattern = ''.join(temp_array)
                    if new_pattern in seen:
                        continue
                    seen.add(new_pattern)
                    queue.append(new_pattern)

            step += 1


        return -1


    def flat_array(self, array):

        pattern = ''
        for r in range(len(array)):
            for c in range(len(array[0])):
                pattern += str(array[r][c])

        return pattern # initial status
