def majority_element(arr):
    counter = 0
    mark = arr[0]
    for i in range(len(arr)):
        if counter == 0:
            mark = arr[i]
            counter = 1
        else:
            if counter!=0 and mark == arr[i]:
                counter += 1

            else:
                counter -= 1
    return mark

print(majority_element([1,2,2,2,3,3,3,3,3,4]))