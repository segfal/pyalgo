

# space complexity: O(1) and time complexity: O(n^2)
def two_sum_nested(nums, target):    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target: 
                return [i, j]
    return []



# space complexity: O(n) and time complexity: O(n)
def two_sum_hash(nums, target):    
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i
    return []

