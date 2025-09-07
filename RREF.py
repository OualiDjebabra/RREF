mat = [
    [0, 2, 1, -1, 8],
    [1, -3, 2, 1, -11],
    [2, -1, 2, 2, -3],
    [1, 1, 1, 0, 4]
]


cols=len(mat[0])
raws=len(mat)
pivot_col=0

for r in range(raws):
    if pivot_col >= cols:
        break

    if mat[r][pivot_col] !=1 and mat[r][pivot_col] !=0:
        factor = mat[r][pivot_col]
        mat[r] = [x/factor for x in mat[r]]
    elif mat[r][pivot_col] ==0:
        for i in range(r+1, raws):
            if mat[i][pivot_col] != 0 and mat[i][pivot_col] ==1:
                mat[r], mat[i] = mat[i], mat[r]
                break
            elif mat[i][pivot_col] !=0:
                mat[r],mat[i]=mat[i], mat[r]
                factor = mat[r][pivot_col]
                mat[r]=[x/factor for x in mat[r]]
                break

    for i in range(raws):
        if i != r:
            factor = mat[i][pivot_col]
            mat[i]=[a-factor*b for a, b in zip(mat[i], mat[r])]
    pivot_col += 1
for row in mat:
    print(row)

        