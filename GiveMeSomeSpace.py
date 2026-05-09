def sum_n(n):
    return n * (n + 1) // 2
print("Sum of first n no.", sum_n(5))

def array_sum(a):
    total = 0
    for i in a:
        total += i
    return total

a = [1, 2, 3, 4, 5]
print("Sum of array is", array_sum(a))

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)
print("Recursive sum" , summ(5))