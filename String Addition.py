class Solution:
    def solve(self, a, b):
        carry = 0
        ans = ""

        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 and j >= 0:
            sum_ = int(a[i]) + int(b[j]) + carry
            actual = sum_ % 10
            carry = sum_ // 10
            ans += str(actual)
            i -= 1
            j -= 1

        if i >= 0:
            while i >= 0:
                sum_ = int(a[i]) + carry
                actual = sum_ % 10
                carry = sum_ // 10
                print(actual)
                ans += str(actual)
                i -= 1
        if j >= 0:
            while j >= 0:
                sum_ = int(b[j]) + carry
                actual = sum_ % 10
                carry = sum_ // 10
                print(actual)
                ans += str(actual)
                j -= 1

        if carry:
            ans += str(carry)

        return ans[::-1]
        
