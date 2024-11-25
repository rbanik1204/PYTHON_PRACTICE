# Two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# Using zip to combine them
combined = zip(names, ages)

# Convert the zip object to a list
combined = list(combined)

print(combined)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
