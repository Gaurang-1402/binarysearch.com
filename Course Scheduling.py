# approach
# it is important to realize that we will not be able
# to complete the courses in a case we have a cycle because how do we determine which course
# to begin with?

# so we need to essentially identify a cycle to return False in the problem
# to do this, we do a regular dfs in a graph. But this time we maintain a set. The purpose
# of the set is to identify if we are in a cycle

# we memoize to speed up the algorithm

# analysis
# we go through each node in the courses so time complexity is
# T = O(n)

# In case of a skewed graph, space complexity is
# S = O(n)


class Solution:
    def solve(self, courses):

        adjacencyList = defaultdict(list)

        for i, course in enumerate(courses):
            adjacencyList[i] = course

        def explore(course, adjacencyList, visited, memo):

            if course in memo:
                return memo[course]

            if course in visited:
                return False

            # base case if a course requires no prereqs, we can take that course
            if adjacencyList[course] == []:
                memo[course] = True
                return memo[course]


            # add the course in the set
            # if we find that any of the prereqs lead
            # to any course that has been visited before (essentially leading to a cycle),
            # we return False
            visited.add(course)

            for prereq in adjacencyList[course]:
                if explore(prereq, adjacencyList, visited, memo) == False:
                    return False

            # remove from visited because it is okay if courses
            # other than the prereqs consider this course as a prereq
            visited.remove(course)

            memo[course] = True
            return memo[course]

        memo = {}
        visited = set()
        for course in adjacencyList.keys():
            if explore(course, adjacencyList, visited, memo) == False:
                return False

        return True

