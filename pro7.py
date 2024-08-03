def insert(arr):
   
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

if __name__ == "__main__":
    li = [1,4,2,8,23]
    print(f"Unsorted list: {li}")
    
    el = insert(li)
    print(f"Sorted list: {el}")