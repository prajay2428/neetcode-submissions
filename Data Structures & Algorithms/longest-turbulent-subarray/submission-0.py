class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        length = 1
        max_length = 1

        if len(arr) == 1:
            return 1
        
        if arr[0] < arr[1]:
            prev_sign = '<'
            length = 2
            max_length = 2

        elif arr[0] > arr[1]:
            prev_sign = '>'
            length = 2
            max_length = 2

        else:
            prev_sign = None

        for i in range(1, len(arr) - 1):

            if arr[i] == arr[i + 1]:
                length = 1
                prev_sign = None
                continue

            if arr[i] < arr[i + 1]:
                curr_sign = '<'
            else:
                curr_sign = '>'

            if prev_sign is None:
                length = 2

            elif curr_sign == prev_sign:
                length = 2

            else:
                length += 1

            prev_sign = curr_sign
            max_length = max(length, max_length)

        return max_length