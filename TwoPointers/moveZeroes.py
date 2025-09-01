def moveZeroes(nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        for num in nums: 
            if num == 0:
                nums.remove(num)
                nums.append(num)
                
        return nums
            
               

n = [0,1,0,3,12]

print(moveZeroes(n))