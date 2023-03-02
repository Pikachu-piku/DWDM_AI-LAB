import random
print("Roll Number: 20115088\nName: Aleem Ahamed Shaik")
print("-----------------------------")
freq = {}
for i in range(0, 6000000):
    die_face = random.randint(1, 6)
    if die_face in freq:
        freq[die_face] += 1
    else:
        freq[die_face] = 1

print("Face\tFrequency")
print("-----------------------------")
for face, frequency in freq.items():
    print(face, "\t", frequency)
