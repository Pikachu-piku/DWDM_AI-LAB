import statistics
print("Roll Number: 20115088\nName: Aleem Ahamed Shaik")
print("-----------------------------")
list = [174, 335, 278, 214, 422, 513, 737, 672, 489, 412,
        1301, 1105, 1123, 1376, 1502, 894, 665, 1704, 1656, 1342]
# minimum, maximum, range, mean, median, variance, and standard deviation

minimum = min(list)
maximum = max(list)
range = maximum-minimum
mean = statistics.mean(list)
median = statistics.median(list)
variance = statistics.variance(list)
standarad_deviation = statistics.stdev(list)

print("Summary Statistics")
print("------------------")
print("Minimum: ", minimum, "\nMaximum: ", maximum, "\nRange: ", range, "\nMean: ", mean,
      "\nMedian: ", median, "\nVariance: ", variance, "\nStandard Deviation: ", standarad_deviation)
