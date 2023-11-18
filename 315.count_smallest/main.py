def countSmaller(nums):
    def mergeSortWithCount(indexes):
        if len(indexes) <= 1:
            return indexes

        mid = len(indexes) // 2
        left = mergeSortWithCount(indexes[:mid])
        right = mergeSortWithCount(indexes[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        i, j = 0, 0
        count_right = 0

        while i < len(left) or j < len(right):
            if j == len(right) or (i < len(left) and nums[left[i]] <= nums[right[j]]):
                merged.append(left[i])
                result[left[i]] += count_right
                i += 1
            else:
                merged.append(right[j])
                count_right += 1
                j += 1

        return merged

    result = [0] * len(nums)
    indexes = list(range(len(nums)))
    mergeSortWithCount(indexes)

    return result

# Exemplo de uso
nums = [5,2,6,1]
output = countSmaller(nums)
print(output)
