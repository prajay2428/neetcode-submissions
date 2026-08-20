class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1:
            return nums[0]

        def houseRobber(arr):
            n = len(arr)

            if n == 1:
                return arr[0]

            dp = [0] * n
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 1],
                    dp[i - 2] + arr[i]
                )

            return dp[n - 1]

        # Don't rob last house
        case1 = houseRobber(nums[:-1])

        # Don't rob first house
        case2 = houseRobber(nums[1:])

        return max(case1, case2)