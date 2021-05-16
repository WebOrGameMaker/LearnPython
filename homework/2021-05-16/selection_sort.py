def selection_sort(nums):
    for i in range(len(nums) - 1):
        minimum = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[minimum]:
                nums[j] = minimum
                
        if minimum != i:
            nums[minimum], nums[i] = nums[i], nums[minimum]
    return nums
