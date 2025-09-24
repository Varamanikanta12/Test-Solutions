# Program-2: Print odd numbers up to given count

n = int(input("Enter the value of a: "))

series = []
for i in range(n):
    series.append(2 * i + 1)


print("Series:", *series)
