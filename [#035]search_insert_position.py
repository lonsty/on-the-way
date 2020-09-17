class Solution:
    offset = 0
    
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid_idx = len(nums) // 2
        mid = nums[mid_idx]
        
        if len(nums) == 1:
            if target > mid:
                return self.offset + 1
            else:
                return self.offset + mid_idx
        
        if target == mid:
            return self.offset + mid_idx
        elif target > mid:
            self.offset += mid_idx
            nums = nums[mid_idx:]
            return self.searchInsert(nums, target)
        else:
            nums = nums[:mid_idx]
            return self.searchInsert(nums, target)
