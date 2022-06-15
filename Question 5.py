st = 'A'
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(st, end="")
        if st == 'Z':
            st = 'A'
        else:
            st = chr(ord(st) + 1)
    print()