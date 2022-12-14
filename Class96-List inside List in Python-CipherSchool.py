# List inside List
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 2d List
# 3 items --› 3 List
print(matrix[2])
for sublist in matrix:
    for i in sublist:
        print(i)
print (matrix[2][0])
s= "string"
print(type(s))
print(type(matrix))
