# https://leetcode.com/problems/3sum/
# https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        solution = []
        nums = sorted(nums)
        # fix i and move l and r in loop
        for i in range(1, len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                # consider case when i l/r equal and l and r equal
                if l==i:
                    l = l + 1
                    continue
                if nums[l] == nums[l+1]:
                    l = l + 1
                    continue
                if nums[r] == nums[r-1]:
                    r = r-1
                    continue
                result = nums[l] + nums[r] + nums[i]
                if result > 0:
                    r = r -1
                if result < 0:
                    l = l+1
                if result == 0:
                    solution.append([nums[l], nums[r] , nums[i]])
                    # ++ l and r while they are equal
                    l = l+ 1
                    r = r-1
        return solution
