class Solution:

    def recur(self, n, k, target, lookup):
		# If target is not reachable then return 0
        if target <= 0 or target > n*k:
            return 0
		# If we are left with one dice and target is equal to any of the faces of dice then we have found a way so return 1
        if n == 1 and target <= k:
            return 1
        if (n, target) not in lookup:
            ways = 0
            for val in range(1, k+1):
				# Use the current dice, update the target as target - current face of dice and recur for remaining target with remaining dices
                ways += (self.recur(n-1, k, target-val, lookup))
            lookup[(n, target)] = ways
        return lookup[(n, target)] 
    
    def solve(self, n, faces, total):
        return self.recur(n, faces, total, {}) % ((10**9) + 7)

        


        
