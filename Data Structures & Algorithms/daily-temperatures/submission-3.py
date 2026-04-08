class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        st.append([temperatures[-1],len(temperatures)-1])
        for i in range(len(temperatures)-2,-1,-1):
            while st and temperatures[i] >= st[-1][0]:
                st.pop()
            if st:
                res[i] = st[-1][1] - i
            st.append([temperatures[i],i])
        return res
