n = int(input("Enter the number of lines of input: "))
print("Enter the input: ")
a = [input() for i in range (n)]

for line in a:
    words = line.split()

    b = [word[::-1] for word in words]

    print(" ". join(b))
