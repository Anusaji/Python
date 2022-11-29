def star(n):

    for i in range(1, n+1):

        print(f"{'*' * i}", end="\n")

    for j in range(n, 0, -1):

        print(f"{'*' * j}", end="\n")

n = int(input("Enter Star Step :"))

star(n)