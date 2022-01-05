class Solution:
    def solve(self, votes):
        voteList = [None for i in range(len(votes) + 1)]
        aCount = 0
        bCount = 0

        def getCandidate(index):
            if votes[index] < 0:
                voteList[index] = 'a'
                return 'a'

            if votes[index] >= len(votes):
                voteList[index] = 'b'
                return 'b'

            if voteList[index] is not None:
                # somewhere in the middle
                return voteList[index]

            voteList[index] = getCandidate(votes[index])
            return voteList[index]

        for i in range(len(votes)):

            if votes[i] < 0:
                voteList[i] = 'a'
                aCount += 1

            elif votes[i] >= len(votes):
                voteList[i] = 'b'
                bCount += 1

            else:
                someCandidate = getCandidate(votes[i])
                if someCandidate == 'a':
                    voteList[i] = 'a'
                    aCount += 1
                elif someCandidate == 'a':
                    voteList[i] = 'b'
                    bCount += 1

        return aCount





        # incorrect below


        # def recursive_helper(votes, low, high):
        #     curr_votes = 0
        #     if low > high:
        #         return 0

        #     if votes[low] < 0:
        #         curr_votes += 1
        #         return curr_votes + recursive_helper(votes, low + 1, high)

        #     if 0 <= votes[low] < len(votes):
        #         some_vote = recursive_helper(votes, votes[low], high)
        #         if some_vote > 0:
        #             curr_votes += 1

        #         else:
        #             curr_votes += recursive_helper(votes, low + 1, high)
        #         return curr_votes

        #     curr_votes += recursive_helper(votes, low + 1, high)

        #     return curr_votes

        # vote_count = recursive_helper(votes, 0, len(votes) - 1)
        # return vote_count

