# approach
# watch this video for an explanation: https://www.youtube.com/watch?v=7ABFKPK2hD4
# essentially, the core idea is to maintain a doubly linked list for the order
# and a hash map to check for membership and get reference to the node at constant time

# the hashmap-doubly linked list combo enables you to modify the order at constant time
# to maintain the doubly linked list, we have two dummy pointers that are constantly being updated
# check comments for explanation


# define this first, it is the doubly linked list node that holds the reference to next and prev
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # maps key to Node(key, val)

        # lrv stands for least recently visited which is the next of lrv
        # lrv is essentially a head dummy Doubly LL node
        self.lrv = Node(0, 0)

        # mrv stands for most recently visited which is the prev of mrv
        # mrv is essentially a tail dummy Doubly LL node
        self.mrv = Node(0, 0)

        # initialize the pointers
        self.lrv.next = self.mrv
        self.mrv.prev = self.lrv

    # removes the node from whatever position it is at
    # because it has been recently evicted or used
    def removeNodeFromList(self, node):
        prevNode = node.prev
        nextNode = node.next

        nextNode.prev = prevNode
        prevNode.next = nextNode

    # insert the node so that it has been most recently visited
    # in the order we're storing
    def insertMostRecentlyVisited(self, node):
        prevMostVisited = self.mrv.prev
        self.mrv.prev = node
        node.next = self.mrv
        prevMostVisited.next = node
        node.prev = prevMostVisited

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # first remove it from the order
            self.removeNodeFromList(node)
            # second make it most recent
            self.insertMostRecentlyVisited(node)
            return node.val
        return -1


    def set(self, key, val):
        # check if you need to change the order of the node in the DLL
        if key in self.cache:
            node = self.cache[key]
            self.removeNodeFromList(node)

        self.cache[key] = Node(key, val)
        node = self.cache[key]
        # make the node most recently visited
        self.insertMostRecentlyVisited(node)


        if len(self.cache) > self.capacity:
            # this was the main purpose of maintaining lrv and mrv pointers
            leastRecentlyVisited = self.lrv.next
            self.cache.pop(leastRecentlyVisited.key)
            self.removeNodeFromList(leastRecentlyVisited)




        
