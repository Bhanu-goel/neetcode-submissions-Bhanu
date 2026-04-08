class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in range(len(tokens)):
            print(tokens[i])
            if tokens[i] not in ('+','-','*','/'):
                st.append(int(tokens[i]))
            else:
                b = st.pop()
                a = st.pop()
                if tokens[i] == '+':
                    st.append(a+b)
                elif tokens[i] == '-':
                    st.append(a-b)
                elif tokens[i] == '*':
                    st.append(a*b)
                elif tokens[i] == '/':
                    st.append(int(a/b))
            print(st)
        return st[-1]
        
