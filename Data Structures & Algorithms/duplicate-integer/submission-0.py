class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        st = set()
        for i in nums:
            if i not in st:
                st.add(i)
                continue
            return True
        return False