import sys

if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}")