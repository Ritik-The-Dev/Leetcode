class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        hashmap = {}

        for i  in  range(len(numbers)):
            newTarget = target - numbers[i]
            if newTarget in hashmap:
                return  [hashmap[newTarget] , i + 1]
            hashmap[numbers[i]] = i + 1

        return -1