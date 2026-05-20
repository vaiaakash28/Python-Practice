# list = [i for i in range (100, 200) for j in range (2, i) if i % j == 0]
# print(list)


for i in range (100, 200):
    for j in range (2, i):
        if i % j == 0:
            break
    else:
        print(i)
