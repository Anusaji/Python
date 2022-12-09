def num_star(n):

    for i in range(1, n + 1):

        for j in range(1, i + 1):

            print(i * j, end=' ')

        print()

num_star(int(input("Enter num star size :")))