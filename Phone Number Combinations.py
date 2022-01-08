# approach

# classic backtracking approach- first create dictionary to map num to the alphabets
# maintain a global list where you can append results

# On each recursive call, we snip off the 0th index of digits and explore the alphabets
# associated with that digit with a shorter digits string.

# we also maintain a currStr variable that is added to based on the char at the first index

# we only add to the result if the digits are useed up

# analysis
# if we take n as len of digits, time complexity is
# T = O(n^4) because we need to generate each combination and in the worst case we get a digit
# that has 4 combinations like 7(pqrs) or 9(wxyz)

# max space is
# S = O(n) due to the space occupied on the stackframes

class Solution:
    def solve(self, digits):
        dialDict = {2: "abc", 3: "def", 4:"ghi",5: "jkl",6: "mno", 7 :"pqrs", 8 : "tuv", 9: "wxyz"}


        result = []
        def explore(digits, currStr):

            if digits == "":
                result.append(currStr)
                return

            options = dialDict[int(digits[0])]

            newDigits = digits[1:]
            for option in options:
                explore(newDigits, currStr + option)

        explore(digits, "")

        return result

            
