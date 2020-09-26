for i in range(int(input())):
	# the first line of input is the number of rows of the array
    # the first line of input is the number of rows of the array
    n = int(input()) 
    a = []
    for i in range(n):
        row = input().split()
        for i in range(len(row)):
            row[i] = int(row[i])
        a.append(row)
    