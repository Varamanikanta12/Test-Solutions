# Program-3: Print odd numbers, special rule for even input

n = int(input("Enter the value: "))

# If we take n is even, take (n-1) terms

count = n if n % 2 != 0 else n - 1

series = []
for i in range(count):
    series.append(2 * i + 1)


print("Series:", ", ".join(map(str, series)))
