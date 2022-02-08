class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result = []

        i = 0; j = 0;

        while i < len(firstList) and j < len(secondList):

            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])


            if lo <= hi:
                result.append([lo, hi])


            if hi == firstList[i][1]:
                i += 1
            else:
                j += 1

        return result
