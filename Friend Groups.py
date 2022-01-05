# approach

# the basic idea is to dfs through the list and mark every node
# that has been visited as visited. After each time you find the first friend in the group
#  the whole group should be marked visited. You then increment numOfGroups
# do this for the entire list

# be careful because the adjacency list is in a list
# and not a dictionary


# analysis
# time complexity is O(n) because you go through n nodes
# T = O(n)

# space complexity is O(n) because max recursion stack is n nodes
#

class Solution:
    def solve(self, friends):

        def explore(member, friends, visited):
            if member in visited:
                return
            if friends[member] == []:
                return

            visited.add(member)

            for friend in friends[member]:
                explore(friend, friends, visited)

            return


        visited = set()
        numOfGroups = 0
        for member in range(len(friends)):
            if member not in visited:
                explore(member, friends, visited)
                numOfGroups += 1

        return numOfGroups
