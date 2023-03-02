print("Roll Number: 20115031\nName: Durgam Priyanka")
print("-----------------------------")
list = []
total = 0
smallest = 1e9
largest = -1
for i in range(0, 7):
    patient_count = int(input("Enter Patient Count on Day "+str(i+1)+": "))
    list.append(patient_count)
    total = total+patient_count
    smallest = min(smallest, patient_count)
    largest = max(largest, patient_count)

average = total/7
print("-----------------------------")
print("Total Patient Count: ", total, "\nAverage Patient Count: ", average,
      "\nMinimum Patient Count: ", smallest, "\nMaximum Patient Count: ", largest)
