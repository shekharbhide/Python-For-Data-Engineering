def get_Equilibrium_Point(arr):

    total_Sum = sum(arr)
    print('total_Sum =',total_Sum)

    left_sum = 0

    for i in range(len(arr)):
        print(f'\narr[{i}] = {arr[i]}')
        print(f'current left sum = {left_sum}')
        print(f'right_sum = {total_Sum} - {left_sum} - {arr[i]}')
        right_sum = total_Sum - left_sum - arr[i]
        print(f'updated right_sum = {right_sum}')

        if left_sum == right_sum:
            print('\nGot equllibrium index: ')
            return i
        else:
            print(f'left sum = {left_sum}+{arr[i]}')
            left_sum += arr[i]
            print(f'updated left sum = {left_sum}')

    return -1


arr = [1,2,0,3]
arr2 = [1,1,1,1]
print(get_Equilibrium_Point(arr))


# # brute force
# def get_Equilibrium_Point(arr):

#     for i in range(len(arr)):
#         print(f'  {arr[:i]} == {arr[i+1:]}')
#         if sum(arr[:i]) == sum(arr[i+1:]):
#             return i

#     return -1


# arr = [1,2,0,3]
# arr2 = [1,1,1,1]
# print(get_Equilibrium_Point(arr2))
