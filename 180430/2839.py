n = int(input());
count = 0
while n % 5: n -= 3;count += 1
print(-1 if n < 0 else n // 5 + count)