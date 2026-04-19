class Solution:
    def sortArray(self,arr):
        if len(arr)<=1:
            return arr
        mid=len(arr)//2
        left=self.sortArray(arr[:mid])
        right=self.sortArray(arr[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        res=[]
        i,j=0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1

        res+=left[i:]
        res+=right[j:]
        return res
