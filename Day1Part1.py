import urllib.request

frequency = 0

file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2018\Day1.txt", "r")

for line in file:
    frequency += int(line)

file.close()

print(frequency)
