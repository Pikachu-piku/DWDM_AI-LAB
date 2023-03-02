import statistics

print("Roll Number: 20115088\nName: Aleem Ahamed Shaik")
print("-----------------------------")
temperatures = [19.5, 19.5, 21.6, 20.2, 19.7, 20.2, 18.6, 17.2, 19.5]

mean = statistics.mean(temperatures)
median = statistics.median(temperatures)
mode = statistics.mode(temperatures)

print(f"Mean temperature: {mean:.1f} °C")
print(f"Median temperature: {median:.1f} °C")
print(f"Mode temperature: {mode:.1f} °C")

