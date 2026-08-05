class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        true_list = [True] * len(candies)
        greatest = max(candies)

        for i in range(len(candies)):
            candies[i] += extraCandies
            if(candies[i] < greatest):
                true_list[i] = False

        return true_list