# approach

# get all permutations of a given number and store it in an array
# to use the same approach as the one we learned, you will have to convert
# the given n int into string->list and then convert it back from list->string->int

# now sort the perms
# finally find the perm given in the question and return the perm after this one else return the first one


# analysis
# since we are finding all the permutations, time complexity is 
# T = O(n!)

# space complexity will depend on number of perms again so
# S = O(n!)


class Solution:
    def solve(self, n):

        def findPermutations(perms):
            result = []
            if len(perms) == 1:
                return [perms[:]]
            else:
                for i in range(len(perms)):
                    currNum = perms.pop(0)
                    incompletePerms = findPermutations(perms)

                    for incompletePerm in incompletePerms:
                        incompletePerm.append(currNum)

                    result.extend(incompletePerms)

                    perms.append(currNum)

                return result
                

        listOfNums = [ str(num) for num in list(str(n))]

        allPermutations = [int("".join(num)) for num in findPermutations(listOfNums)]

        allPermutations.sort()

        for i, perm in enumerate(allPermutations):
            if i + 1 < len(allPermutations) and perm == allPermutations[i + 1]:
                continue

            if perm == n:
                return allPermutations[i + 1] if i + 1 < len(allPermutations) else allPermutations[0]
