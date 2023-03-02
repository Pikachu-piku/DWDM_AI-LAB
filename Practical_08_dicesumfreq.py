from collections import OrderedDict
print("Roll Number: 20115088\nName: Aleem Ahamed Shaik")
print("-----------------------------")
list = [1, 2, 3, 4, 5, 6]

freq = {}
for i in range(0, 6):
    sum = list[i]
    for j in range(0, 6):
        sum = sum+list[j]
        if sum in freq:
            freq[sum] += 1
        else:
            freq[sum] = 1

        sum -= list[j]


freq = OrderedDict(sorted(freq.items()))
print("Sum\tFrequency")
#print("-----------------")
max_freq = -1
min_freq = 1e9
max_occuring_sums = []
min_occuring_sums = []

for sum, frequency in freq.items():
    print(sum, "\t", frequency)
    if (frequency > max_freq):
        max_occuring_sums.clear()
        max_freq = frequency
        max_occuring_sums.append(sum)
    elif (frequency == max_freq):
        max_occuring_sums.append(sum)

    if (frequency < min_freq):
        min_occuring_sums.clear()
        min_freq = frequency
        min_occuring_sums.append(sum)
    elif (frequency == min_freq):
        min_occuring_sums.append(sum)

#print("-----------------")
print("Most frequently Occuring Sums: ", max_occuring_sums,
      "\nLeast Frequently Occuring Sums: ", min_occuring_sums)
