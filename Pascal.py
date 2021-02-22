# Andrew Stade
# 1/20/2021
# afs18c
# The program in this file is the individual work of Andrew Stade.


n = int(input("Enter number of rows: "))
tri = []
for i in range(n):
    tri.append([])
    tri[i].append(1)
    for j in range(1, i):
        tri[i].append(tri[i-1][j-1] + tri[i-1][j])
    if(n != 0):
        tri[i].append(1)

for i in range(n):
    for j in range(0, i + 1):
        print(tri[i][j],end = " ")
    print()