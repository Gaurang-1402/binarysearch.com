class Solution:
    def solve(self, lst):
        # find pivot
        low = 0

        high = len(lst) - 1

        mid = low

        while low < high:
            mid = (low + high) // 2

            if (lst[mid] > lst[high]):
                low = mid + 1

            else:
                # (lst[mid] <= lst[high])
                high = mid

        return lst[low-1] # low is the pivot










        
