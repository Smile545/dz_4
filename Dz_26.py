def rec(n, y):
    if y == 0:
        return 1
    else:
        return n * rec(n, y-1)
    
a = int(input("Введите число "))
b = int(input("Введите число "))
print(rec(a, b))