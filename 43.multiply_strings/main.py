class Solution(object):
    def multiply(self, num1, num2):

        num1 = [int(digit) for digit in reversed(num1)]
        num2 = [int(digit) for digit in reversed(num2)]

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                result[i + j] += num1[i] * num2[j]
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(str(digit) for digit in reversed(result))