# approach
# 1) extend the shorter string with 0s to match the longer string
# 2) traverse the string from reverse and maintain a carry var
# do bin addition and update the carry var based on the different cases
# add the outcome of the addition of a column to the finalStr
# 3()

# analysis
# you go through the entire longer string between a and b so time complexity is
# T = O(n)

# no extra space saved
# S = O(k)

class Solution:
    def solve(self, a, b):

        finalStr = ""

        # 1) extend
        if len(a) > len(b):
            b = "0" * (len(a) - len(b)) + b

        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a

        carry = 0
        i = len(a) - 1
        finalStr = ""

        while i >= 0:
            if (a[i] == "1" and b[i] == "1"):
                if carry == 1:
                    # case1: 3 1s
                    finalStr = "1" + finalStr
                    carry = 1
                else:
                    # case2: 2 1s
                    finalStr = "0" + finalStr
                    carry = 1

            elif (a[i] == "1" and b[i] == "0" or a[i] == "0" and b[i] == "1"):
                if carry == 1:
                    # case2: 2 1s
                    finalStr = "0" + finalStr
                    carry = 1
                else:
                    # case3: 1 1s
                    finalStr = "1" + finalStr
                    carry = 0
            else:
                # 0 0
                if carry == 1:
                    # case3: 1 1s
                    finalStr = "1" + finalStr
                else:
                    # case4: 0 1s
                    finalStr = "0" + finalStr
                carry = 0
            i -= 1

        if carry == 1:
            finalStr = "1" + finalStr

        return finalStr
