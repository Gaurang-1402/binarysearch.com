class Solution:
    def solve(self, n):

        low = 1

        high = n

        while low <= high:
            mid = (low + high) //2
            if  (mid*mid<=n and (mid+1)*(mid+1)>n):
                return mid
            elif n // mid > mid:
                low = mid + 1
            elif n // mid < mid:
                high = mid - 1


        return mid




        
