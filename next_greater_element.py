stack = []
a = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
res = [-1] * len(a)
n=len(a)
for i in range(2*n-1, -1, -1):  # Changed range for 20 iterations
    while stack and stack[-1] <= a[i % len(a)]:
        stack.pop()
    if stack:
        res[i % len(a)] = stack[-1]
    stack.append(a[i % len(a)])
print(res)
    # Output: [10, -1, 6, 6, 2, 6, 7, 7, 9, 9, 10]
    # Update for i = 19
    # stack = []
    # a[8] = 9
    # stack = [9]
    # res = [-1, -1, -1, -1, -1, -1, -1, -1, 9, -1, -1]

    # Update for i = 18
    # stack = [9]
    # a[7] = 7
    # res[7] = 9
    # stack = [9, 2]
    # res = [-1, -1, -1, -1, -1, -1, -1, 9, 9, -1, -1]

    # Update for i = 17
    # stack = [9, 2]
    # a[6] = 6
    # stack = [9]
    # res[6] = 9
    # res = [-1, -1, -1, -1, -1, -1, 9, 9, 9, -1, -1]

    # Update for i = 16
    # stack = [9]
    # a[5] = 2
    # res = [-1, -1, -1, -1, -1, -1, 9, 9, 9, -1, -1]

    # Update for i = 15
    # stack = [9]
    # a[4] = 1
    # res = [-1, -1, -1, -1, -1, -1, 9, 9, 9, -1, -1]

    # Update for i = 14
    # stack = [9]
    # a[3] = 2
    # stack = [9, 2]
    # res = [-1, -1, -1, -1, -1, -1, 9, 9, 9, 2, -1]

    # Update for i = 13
    # stack = [9, 2]
    # a[2] = 4
    # stack = [9]
    # res[2] = 9
    # res = [-1, -1, 9, -1, -1, -1, 9, 9, 9, 2, -1]

    # Update for i = 12
    # stack = [9]
    # a[1] = 10
    # stack = [10]
    # res[1] = 10
    # res = [-1, 10, 9, -1, -1, -1, 9, 9, 9, 2, -1]

    # Update for i = 11
    # stack = [10]
    # a[0] = 3
    # stack = [10, 3]
    # res[0] = 10
    # res = [10, 10, 9, -1, -1, -1, 9, 9, 9, 2, -1]

# The loop continues similarly for the remaining iterations



