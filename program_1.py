
'''
1.  Print the count of the element in the list.
For e.g [1,4,2,6,2,4,1,2]
The output should be printing the count of each element like
1-2
4-2
2-3, etc
The output should be a dictionary. Code it with two approaches 1. With in-built function 2. Write your own function without using any in-built
'''

# Using in-built function

arr = [1,4,2,6,2,4,1,2]
store = dict()

for i in arr:
    store[i] = arr.count(i)
    
print(store)


# Making my own function

def findCounts(arr, n):
    i = 0
    while i<n:
        if arr[i] <= 0:
            i += 1
            continue
        elementIndex = arr[i] - 1
        if arr[elementIndex] > 0:
            arr[i] = arr[elementIndex]
            arr[elementIndex] = -1
        else:
            arr[elementIndex] -= 1
            arr[i] = 0
            i += 1
    print ("Below are counts of all elements")
    store = dict()
    for i in range(len(arr)):
        store[i+1] = abs(arr[i])

    print(store)

arr = [1,4,2,6,2,4,1,2] 
findCounts(arr, len(arr)) 

  
