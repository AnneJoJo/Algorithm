

def reshapeArray(arr):
    """
    :param arr: ["MUL 2", "ADD 3"]
    :return: ["MUL", "2", "ADD", "3"]
    """
    newArr = [item for s in arr for item in s.split()]
    return  newArr


print(reshapeArray(["MUL 2", "ADD 3"]))