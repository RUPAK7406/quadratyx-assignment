def get_transpose_of_matrix(matrix, m, n):
    transpose_matrix = []
    for i in range(n):
        row= []
        for j in range(m):
            row.append(matrix[j][i])
        transpose_matrix.append(row)
    return transpose_matrix

def reverse_columns(transposed_matrix):
    for i in range(n):
        j = 0
        k = n-1
        while j < k:
            t = transposed_matrix[j][i]
            transposed_matrix[j][i] = transposed_matrix[k][i]
            transposed_matrix[k][i] = t
            j += 1
            k -= 1
    return transposed_matrix
m, n = input().split()
m, n = int(m), int(n)

num_list = []
for i in range(m):
    list_a = list(map(int, input().split()))
    num_list.append(list_a)
    
transposed_matrix = get_transpose_of_matrix(num_list, m, n)
reversed_columns =reverse_columns(transposed_matrix)
print(reversed_columns)