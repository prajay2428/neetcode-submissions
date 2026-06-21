class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []

        for num in nums1:
            idx = nums2.index(num)

            next_greater = -1

            for j in range(idx + 1, len(nums2)):
                if nums2[j] > num:
                    next_greater = nums2[j]
                    break

            answer.append(next_greater)

        return answer