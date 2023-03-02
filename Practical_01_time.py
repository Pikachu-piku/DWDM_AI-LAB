
print("Roll Number: 20115031\nName: Durgam Priyanka")
print("-----------------------------")
input_seconds = int(input("Enter seconds: "))
hours = int(input_seconds/3600)
input_seconds = input_seconds-(hours*3600)
minutes = int(input_seconds/60)
input_seconds = input_seconds-(60*minutes)
seconds = input_seconds
print(hours, "-", minutes, "-", seconds)
