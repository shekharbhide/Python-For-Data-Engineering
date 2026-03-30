def hasArrayTwoCandidates(arr, n, x):
        # code here
        mpp = {}
        for i in range(n):
            num = arr[i]
            moreNeeded = x - num
            if moreNeeded in mpp:
                return True
            mpp[num] = i
        return False     

arr= list(map(int, input().split()))
n = len(arr)
x = int(input())
print(hasArrayTwoCandidates(arr,n,x))