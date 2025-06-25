# Swap Variables

a = "any value"
b = "another value"

print(f"a is {a}")
print(f"b is {b}")

a, b = b, a

print(f"a is now {a}")
print(f"b is now {b}")

# For a general input

print("Enter the value of a: ")
a = input()

print("Enter the value of b:")
b = input()

print(f"a is {a}")
print(f"b is {b}")

a, b = b, a

print(f"a is now {a}")
print(f"b is now {b}")

print("This is called swapping of variables using a one-line code.")