# approach

# we use bfs in tree (also known as level order traversal)
# we maintain a queue to do level order traversal

# on each while loop iteration, we know that we are on a new level
# the queue will only have nodes on this level in the beginning

# since we need leftview, we pop and add the val of the first node
# (if it was right view, we would keep popping and wait to pop the rightmost node before appending)

# now we add the children of currNode if they are not None
# then traverse the queue the number of times = len of queue
# save lenOfQueue at the beginning of the loop because you add and remove nodes

# keep popping and adding children of nodes in current level

# analysis
# Time complexity is linear because we go through each node in level order traversal
# T = O(n)

# Space complexity is also n nodes because len of queue can get n at most if we had a
# linear binary tree
# S = O(n)

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def solve(self, root):

        queue = deque([root])

        leftView = []
        while len(queue) > 0:
            curr = queue.popleft()

            leftView.append(curr.val)

            # save this first because
            # later you will modify the size of the queue in the for loop
            lenOfQueue = len(queue)

            if curr.left is not None:
                queue.append(curr.left)

            if curr.right is not None:
                queue.append(curr.right)

            for i in range(lenOfQueue):
                temp = queue.popleft()
                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)

        return leftView
