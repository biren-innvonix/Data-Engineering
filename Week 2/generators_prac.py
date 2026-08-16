def count_to(n):
    count = 1
    while(count <= n):
        yield count
        count += 1

# for num in count_to(5):
#     print(num)

x = count_to(10000000)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
