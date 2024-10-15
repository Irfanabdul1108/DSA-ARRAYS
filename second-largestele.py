class Solution:
    def getSecondLargest(self, arr):
        maxi=max(arr)
        smaxi=-1
        for i in arr:
            if i>smaxi and i!=maxi:
                smaxi=i
        return smaxi
    