
numvertices = int(input("Enter number of vertices: "))
numedges = int(input("Enter number of edges: "))


adjmatrix = [[0]*numvertices for x in range(numvertices)]
adjlist = [[] for x in range(numvertices)]

for edges in range(numedges):
    tempedge = input("Enter Edge: ")
    tempnums = tempedge.split(" ")
    adjlist[int(tempnums[0])].append(int(tempnums[1]))
    adjmatrix[int(tempnums[0])][int(tempnums[1])] = 1


print(" ")
print("List:")
print(adjlist)

print(" ")
print("Matrix:")
for x in range(numvertices):
    print(adjmatrix[x])

