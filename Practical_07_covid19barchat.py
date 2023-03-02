
import matplotlib.pyplot as plt
print("Roll Number: \nName: ")
print("-----------------------------")
list = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
        1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]

freq = {}

for i in range(0, len(list)):
    freq[i] = list[i]

plt.bar(freq.keys(), freq.values(), color='g')
plt.xlabel("Days")
plt.ylabel("Number of Cases")
plt.title("Covid-19")
for i in range(0, len(list)):
    plt.text(i, list[i], list[i], ha='center',
             va='bottom', color='r', fontsize=7)
plt.show()
