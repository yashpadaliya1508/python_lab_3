def selec(arr):
    n = len(arr)
    
    for i in range(n):
        idx = i
        for j in range(i+1, n):
            if arr[j] < arr[idx]:
                idx = j
                
        arr[i], arr[idx] = arr[idx], arr[i]

    return arr

if __name__ == "__main__":
    li = [22,13,4,8,17,26,53,4]
    print(f"Unsorted list: {li}")
    
    el = selec(li)
    print(f"Sorted list: {el}")