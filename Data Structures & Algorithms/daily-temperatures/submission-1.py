class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)-1,-1,-1):
            if not st:
                res[i] = 0
                st.append([temperatures[i],i])
            else:
                if temperatures[i] < st[-1][0]:
                    res[i] = st[-1][1] - i
                    st.append([temperatures[i],i])
                else:
                    while st and temperatures[i] >= st[-1][0]:
                        st.pop()
                    if not st:
                        res[i] = 0
                    else:
                        res[i] = st[-1][1] - i
                    st.append([temperatures[i],i])
        return res
