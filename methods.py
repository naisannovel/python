# range(start, end, step)
a = range(50)   # treat as end
print(a)        # range(0, 50)

r = range(0, 50, 5)
print(r)        # range(0, 50, 5)

print(r[1])     # 0
print(r[2])     # 5
print(r[3])     # 10

print(list(r))  # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
