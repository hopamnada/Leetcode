class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
                return arr
            arr[i] = max(arr[i+1:len(arr)])
        