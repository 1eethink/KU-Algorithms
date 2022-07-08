def max_subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low+high)/2)
        left_low, left_high, left_sum = max_subarray(A, low, mid)
        right_low, right_high, right_sum = max_subarray(A, mid+1, high)
        cross_low, cross_high, cross_sum = max_cross_subarray(A, low, mid, high)

        if (left_sum >= right_sum) and (left_sum >= cross_sum):
            return left_low, left_high, left_sum
        elif (right_sum >= left_sum) and (right_sum >= cross_sum):
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum



def max_cross_subarray(A, low, mid, high):
    if A[mid] > 0:
        left_sum = -A[mid] - 1
    else:
        left_sum = A[mid] - 1
    #left_sum = -math.inf
    sum = 0

    for i in range(mid, low-1, -1):
        sum = sum + A[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    if A[mid+1] > 0:
        right_sum = -A[mid+1] - 1
    else:
        right_sum = A[mid+1] - 1

    #right_sum = -math.inf
    sum = 0

    for j in range(mid+1, high+1):
        sum = sum + A[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return max_left, max_right, left_sum+right_sum

A=[]
n = int(input())
for i in range(n):
    A.append(int(input()))

low = 0
high = len(A)-1
B = max_subarray(A, low, high)

for i in B:
    print(int(i))

