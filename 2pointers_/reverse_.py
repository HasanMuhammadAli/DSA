def reverse_arr_str(listt):
    left, right = 0, len(listt)-1
    while left < right:
        listt[left], listt[right] = listt[right], listt[left]
        left += 1
        right -= 1
    return listt

arr = [0, 1, 2]
print(reverse_arr_str(arr))