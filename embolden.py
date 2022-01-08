# approach
# The idea is simple: build a list of "flagged indices" which indicate that we should bold letters at this index. Then when we look through the original text, we have ranges to open and close our bold tags.

# Create a painting list of indices to paint
# Populate with values to be painted, based on index.
# Go through the original text and insert bold tags before and after we have found a string in indices to bold

# analysis
# Time Complexity
# O(n * m) where n is len(text) and m is len(max_word) in pattern.

# Space Complexity
# O(n), bolded stores n length values

"""
text = "abcdefg"

patterns = ["bc", "ef"]

convert letters to list of yes or not bold:

0:False
1:True
2:True
3:False
4:True
5:True
6:False

go through string and turn ranges back into bolded

"""


class Solution:
    def solve(self, text, patterns):
        n = len(text)
        bolded = [False] * n

        for pat in patterns:
            start = text.find(pat)

            while start != -1:
                for i in range(start, start + len(pat)):
                    bolded[i] = True

                start = text.find(pat, start + 1)

        ans = []
        idx = 0

        while idx < n:
            if bolded[idx]:
                ans.append("<b>")

                while idx < n and bolded[idx]:
                    ans.append(text[idx])
                    idx += 1

                ans.append("</b>")
            else:
                ans.append(text[idx])
                idx += 1

        return "".join(ans)
