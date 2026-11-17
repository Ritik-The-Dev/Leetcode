class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        
        pairs={}

        for num in arr:
            pairs[num] = pairs.get(num , 0) + 1

        isUnique = {}

        for _,value in pairs.items():
            if value in isUnique:
                return False
            isUnique[value] = True

        return True
        