class Solution:

    # O(nlogn) | O(n)

    def solve(self, trips, capacity):

        carList = []

        for start, end, people in trips:
            carList.append((start, people))
            carList.append((end, -people))

        carList.sort()



        for _, people in carList:
            capacity -= people
            if capacity < 0:
                return False

        return True

