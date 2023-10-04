a1 = int(input())
b1 = int(input())

a2 = int(input())
b2 = int(input())


start = max(a1, a2)
end = min(b1, b2)

if start <= end:
    print(start, end)
else:
    print("пустое множество")

