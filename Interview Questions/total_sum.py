arr = [1,2,3,4,5,6,7,8]

def total_sum(arr):
    sum = 0

    for num in arr:
        sum = sum + num

    return sum

print(total_sum(arr))