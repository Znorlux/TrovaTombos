def greedy(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2, reverse=True)

    result = 0
    for i in range(0,len(arr1)):
        result += arr1[i] * arr2[i]
    return result
        
list1 = [6,1,9,5,4]
list2= [3,4,8,2,4]
print(greedy(list1,list2))