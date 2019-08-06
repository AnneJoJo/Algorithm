def sort_binary_arr(arr):
    #[1,0,1,0,1,0,0,1]

    faster = 1
    i = 0
    while faster < len(arr):

        if arr[i] == 1 and arr[faster] == 0:
            arr[i],arr[faster] = arr[faster], arr[i]
            i += 1
        elif arr[i] == 0:
            i+= 1

        faster += 1
    return arr

print(sort_binary_arr([1,0,0,0,1,1,1,1,1,0]))

