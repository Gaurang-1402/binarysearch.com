class Solution:
    def solve(self, s):

        # edge cases
        s = s.split()
        n = len(s)
        q = deque((i, 0) for i in range(n))
        ans = []

        while True:
            tmp = ""
            for _ in range(n):
                cur_str, cur_idx = q.popleft()
                if cur_idx >= len(s[cur_str]):
                    tmp += " "
                    q.append((cur_str, cur_idx + 1))
                else:
                    tmp += s[cur_str][cur_idx]
                    q.append((cur_str, cur_idx + 1))

            res = tmp.rstrip()
            if res != "":
                ans.append(res)
            else:
                break

        return ans

        # # main

        # split_list = s.split(" ")

        # max_len = 0

        # max_len_idx = 0
        # for idx, word in enumerate(split_list):
        #     if len(word) >= max_len:
        #         max_len_idx = idx

        #     max_len = max(max_len, len(word))



        # result = []

        # for idx in range(max_len):
        #     curr_word= ""

        #     for word_idx, word in enumerate(split_list):
        #         if idx >= len(word) and word_idx > max_len_idx:
        #             continue
        #         elif idx >= len(word):
        #             curr_word += " "
        #         else:
        #             curr_word += word[idx]

        #     result.append(curr_word)


        # return result
        
