# intuition
# since we are dealing with 24 hours, we can use the constant number of minutes which is 24 * 60 to test
# the first permutation we hit after our (current mins) % (60 * 24)  which will be our answer since we can only
# go forward in clock

# implementation
# set can be used to maintain the characters, we first convert 24 hour string time to mins time, increment minutes,
# then we convert mins time to 24 hour string time and check if all the chars in this 24 hour format are present in
# the set

# analysis
# time at most is 1439 iterations so time complexity is
# T = O(k)

# we only store 4 chars in our set so space complexity is
# S = O(k)

class Solution:
    def solve(self, s):

        hours, minutes = s.split(":")

        currMins = int(hours) * 60 + int(minutes)

        availableDigits = set()
        availableDigits.add(hours[0])
        availableDigits.add(hours[1])
        availableDigits.add(minutes[0])
        availableDigits.add(minutes[1])

        while True:
            # use while True because it is certain that we will come across
            # at least one permutation as we increment minutes so the return statment will certainly be hit

            currMins = (currMins + 1) % (24 * 60) # % by (24 * 60) to ensure we are in the [0 to 1439 mins (24 * 60)] range


            currTime = str((currMins // 60) // 10) + str((currMins // 60) % 10) + str((currMins % 60) // 10) + str((currMins % 60) % 10)
            # interesting way to extract hours firstDigit, hours secondDigit, minutes firstDigit, minutes secondDigit

            nextClosest= True
            for char in str(currTime):
                if char not in availableDigits:
                    nextClosest = False

            if nextClosest:
                # format the answer appropriately before returning
                return str(currTime)[:2] + ":" + str(currTime)[2:]


