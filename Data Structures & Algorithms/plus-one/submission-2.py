class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits

        for i in range(len(digits)-1, -1, -1):
            if i == 0 and digits[i] == 9:
                digits[i] = 0
                digits.insert(0, 1)
            elif digits[i] != 9:
                digits[i] = digits[i] + 1
                break
            else:
                digits[i] = 0

        return digits