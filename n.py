import random

def prob(arr):
    print("It is traversing in row major order. Hence result is in row major order itself")
    res = []
    for i in range(4):
        for j in range(4):
            k = min(arr[i*2][j*2], arr[i*2+1][j*2],
                    arr[i*2][j*2+1], arr[i*2+1][j*2+1])
            if arr[i*2][j*2] == k:
                res.append([i*2, j*2])
            elif arr[i*2 + 1][j*2] == k:
                res.append([i*2+1, j*2])
            elif arr[i*2][j*2+1]:
                res.append([i*2, j*2+1])
            else:
                res.append([i*2+1, j*2+1])
    print("Result line by line")
    for i in res:
        print(i)
    
    print("Result in matrix form")
    for i in range(4):
        for j in range(4):
            print( "(" + str(res[i*4 + j]) + ")", end = " ")
        print()



arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8]
]

arr2 = []
for i in range(8):
    arrin = []
    for j in range(8):
        k = random.randint(1,1000)
        arrin.append(k)
    arr2.append(arrin)

arr3 = []
print("Enter 64 numbers line by line, so 64 lines")
for i in range(8):
    arrin = []
    for j in range(8):
        arrin.append(input())
    arr3.append(arrin)

#choose array
for i in arr3:
    print(i)
prob(arr3)
