class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        if len(A) > len(B):
            A,B = B,A
        
        l1 = len(A)
        l2 = len(B)
        total = l1+l2
        half = (total+1)//2

        l=0
        r=l1

        while l<=r:
            i = l + (r - l)//2
            j = half - i

            Aleft = A[i-1] if i > 0 else -float('infinity')
            Aright = A[i] if i < l1 else float('infinity')

            Bleft = B[j-1] if j > 0 else -float('infinity')
            Bright = B[j] if j < l2 else float('infinity')

            if Aleft <= Bright and Bleft <= Aright:
                if (l1+l2)&1:
                    return max(Aleft,Bleft)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
        return 0