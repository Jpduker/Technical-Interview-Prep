class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1

        while l<=r:
            mid = floor((l+r)/2)
            if target ==nums[mid]:
                return True
            #right portiion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target<nums[l] :
                    l = mid+1
                else:
                    r = mid-1
            #left portion
            else:
                if target <nums[mid] or target >nums[r]:
                    r=mid-1
                else:
                    l=mid+1
        return False