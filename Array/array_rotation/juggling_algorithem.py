# Array rotation with juggling algorithem
# Defination: https://www.geeksforgeeks.org/array-rotation/
# Array Rotation Video: https://www.youtube.com/watch?v=viaha1SnpT4
# Calculate GCD: https://www.youtube.com/watch?v=JYn-XG-d7AA
# Online executor: https://pythontutor.com/python-debugger.html


# arr   =  {1,2,3,4,5,6,7,8,9,10,11,12}
# index     0,1,2,3,4,5,6,7,8,9 ,10,11
# N = 12
# D = 3

def rotate(A, N, D):
    end = GCD(N, D)
    for i in range(end): # 0,1,2
        temp = A[i]
        j = i
        while(True):
            k = j + D # k = 0 + 3
            if k >= N: # 12>=12
                k = k - N # k = 12 - 12 
            if k == i:
                break
            # assing the values
            A[j] = A[k] #  A[0] = A[3]           
            j = k # j = 3
        arr[j] = temp # arr[12] = 1

def GCD(a, b):
    if b==0:
        return a
    else:
        return GCD(b, a%b)

arr = [1,2,3,4,5,6,7,8,9,10,11,12]
D = 3
rotate(arr, len(arr), D)
print(arr)