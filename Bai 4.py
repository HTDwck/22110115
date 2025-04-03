def fibonacci(n):
    if n < 0:
        return "Số nhập vào phải lớn hơn hoặc bằng 0"

    fib = [0] * (n + 1)
    if n > 0:
        fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

n = int(input("Nhập số nguyên n: "))
print(f"Số Fibonacci thứ {n} là: {fibonacci(n)}")
