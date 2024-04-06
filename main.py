from math import ceil
import json

data = json.load(open('data.json', 'r', encoding='utf-8'))

# Calculate the gems needed
sum = 0
for i in range(1, 1500):
    sum += data[str(i)]

print(f"Total gems needed: {sum}")

# Calculate time to watch
def euclidean_division(dividend, divisor):
    q = dividend // divisor
    r = dividend % divisor

    return q, r

ads_length = 40
t = ads_length * sum

"""
# Adds the 4 hours between each "sessions" (one session equals 20 gems)
# *not sure this is how it should be done but hey it's there

session = ceil(sum / 20)
t += (session * (4*3600))
"""

min, sec = euclidean_division(t, 60)
h, min = euclidean_division(min, 60)
d, h = euclidean_division(h, 24)

print(f"{d}d {h}h {min}min {sec}sec")
