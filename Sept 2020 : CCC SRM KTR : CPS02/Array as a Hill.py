def checkForHill(arr, n): 
      
    # Cover first strictly increasing part 
    i = 1
    while (i < n and arr[i] > arr[i - 1]): 
        i += 1
  
    # Cover middle equal part 
    while (i < n and arr[i] == arr[i - 1]): 
        i += 1
  
    # Cover last decreasing part 
    while (i < n and arr[i] < arr[i - 1]): 
        i += 1
  
    # Return true if we reached end. 
    return (i == n) 
  
if __name__ == '__main__': 
    n = int(input())
    arr = list(map(int, input().split()))

    if (checkForHill(arr, n)): 
        print("yes") 
    else: 
        print("no") 
