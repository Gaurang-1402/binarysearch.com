class Solution:
    def solve(self, message):

        memo = {len(message) : 1}
        def explore(index):

            if index in memo:
                return memo[index]

            if message[index] == '0':
                return 0

            result = explore(index + 1)

            if (index + 1 < len(message) and (message[index] == '1' or message[index] == '2' and message[index + 1] in '0123456')):
                result += explore(index + 2)

            memo[index] = result
            return result

        return explore(0)


    
