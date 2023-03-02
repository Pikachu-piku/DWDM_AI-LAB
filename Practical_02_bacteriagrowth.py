print("Roll Number: 20115031\nName: Durgam Priyanka")
print("-----------------------------")


def growth(initial_count, n):
    if (n == 0):
        return initial_count

    return initial_count*2*n


initial_count = 200
list = []
for i in range(0, 4):
    list.append(growth(initial_count, i*5))


print("Duration(in Hours)\tBacteria_Count")
print("------------------------------------")

for i in range(0, 4):
    print(i*5, "\t\t\t", list[i])
