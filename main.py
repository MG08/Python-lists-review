nums = [11,56,87,45,31,67,92,51,39,74,46]

print(nums)
nums.sort()
print(nums)

print("The smallest number in the list is", nums[0])
print("The median number in the list is", nums[5])
print("The biggest number in the list is", nums[10])

nums2 = []
for i in range(90,110):
    nums2.append(random.randrange(0,100))
    
print(nums2)

smallest = nums2[0]
for i in range(0,11):
    if nums2[i]<smallest:
        smallest = nums2[i]
        
print("The smallest number in the list is", nums2[0])
