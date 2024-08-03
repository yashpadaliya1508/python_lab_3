def seq(list1, n, key): 
    for i in range(0, n):  
        if (list1[i] == key):  
            return i  
    return -1  
 
list1 = [1,3,5,8,10,23,35]  
print(list1,"\n")
key = int(input("Enter The No :- "))
  
n = len(list1)  
res = seq(list1, n, key)  
if(res == -1):  
    print("Element not found in List....")  
else:  
    print("Element found at index: ", res)  