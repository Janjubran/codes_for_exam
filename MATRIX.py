#%%
def mult_board(m,n):
    board = []
    for i in range(1, n+1):
        row = []
        for j in range(1, m+1):
            row.append(i * j)
        board.append(row)
    return board
m = 5
n = 5
print(mult_board(m,n))
# %%
def transposed(lst):
    transposed_lst = []
    for i in range(len(lst[0])):
        temp = []
        for j in range(len(lst)):
            temp.append(lst[j][i])
        transposed_lst.append(temp)
    return transposed_lst
lst = [[1,2,3],
       [4,5,6]]
print(transposed(lst))
# %%
