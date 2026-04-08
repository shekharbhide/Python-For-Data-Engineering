def find_leaders(arr: list[int]) -> list[int]:
    leaders = []
    leaders.append(arr[-1])
    right_max = arr[-1]
    for i in range(len(arr)-2, -1, -1):
        if arr[i] >= right_max:
            leaders.append(arr[i])
            right_max = arr[i]

    
    return leaders[::-1]


arr = [16, 17, 4, 3, 5, 2]
print(find_leaders(arr))

# def find_leaders(arr: list[int]) -> list[int]:
#     leaders = []
    
#     for i in range(len(arr) - 1):
#         if arr[i] >= max(arr[i+1:]):
#             leaders.append(arr[i])
            
#     leaders.append(arr[-1])   # same level as for loop
    
#     return leaders


# arr = [16, 17, 4, 3, 5, 2]
# print(find_leaders(arr))




# def find_leaders(arr: list[int]) -> list[int]:
# 	# Write your code here
# 	leaders = []
# 	for left_i in range(len(arr)):
# 		isLeader = True 
		
# 		for right_i in range(left_i + 1, len(arr)):
# 			if arr[right_i] > arr[left_i]:
# 				isLeader = False
				
# 		if isLeader:
# 			leaders.append(arr[left_i])
	
# 	return leaders
# 	#return [-1]


# arr = [16, 17, 4, 3, 5, 2]
# print(find_leaders(arr))