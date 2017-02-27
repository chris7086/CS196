
# coding: utf-8

# In[234]:

def transpose_matrix(matrix):
    a=[]
    length = len(matrix[0])
    for i in range (0,len(matrix[0])):
        j=[]
        for elem in matrix:
            if length != len(elem):
                return None
            j.append(elem[i]) 
        a.append(j)
    return a


# In[235]:

def orthogonal_vectors(matrix):
    a = matrix[0][0]*matrix[0][1]+matrix[1][0]*matrix[1][1]+matrix[2][0]*matrix[2][1]
    b = matrix[0][0]*matrix[0][2]+matrix[1][0]*matrix[1][2]+matrix[2][0]*matrix[2][2]
    c = matrix[0][1]*matrix[0][2]+matrix[1][1]*matrix[1][2]+matrix[2][1]*matrix[2][2]
    if (a==b==c==0):
        return True
    else:    
        return False


# In[236]:

def winner_of_tic_tac_toe(game):
    if game[0][0]==game[0][1]==game[0][2]:
        return (game[0][0] + " wins!")
    if game[1][0]==game[1][1]==game[1][2]:
        return (game[1][0] + " wins!")
    if game[2][0]==game[2][1]==game[2][2]:
        return (game[2][0] + " wins!")
    if game[0][0]==game[1][0]==game[2][0]:
        return (game[0][0] + " wins!")
    if game[0][1]==game[1][1]==game[2][1]:
        return (game[0][1] + " wins!")
    if game[0][2]==game[1][2]==game[2][2]:
        return (game[0][2] + " wins!")
    if game[0][0]==game[1][1]==game[2][2]:
        return (game[0][0] + " wins!")
    if game[0][2]==game[1][1]==game[2][0]:
        return (game[0][2] + " wins!")
    else:
        return ("Draw!")


# In[237]:

def spiral_matrix(arr):
    result = []
    cycle = 0
    while (arr != []):
        for elem in arr[0]:
            result.append(elem)
            if (arr == []):
                return result
        del arr[0]
        for elem in arr:
            result.append(elem[len(elem)-1])
            del elem[len(elem)-1]
        if (arr == []):
            return result
        arr.reverse()
        for elem in arr:
            elem.reverse()


# In[238]:

def flatten_list(arr):
    result = []
    for elem in arr:
        for a in elem:
            result.append(a)
    return result


# In[239]:

def sort_matrix(mat):
    flat = []
    result = []
    for row in mat:
        for col in row:
            flat.append(col)
    for row in mat:
        sub = []
        for col in mat[0]:
            a=max(flat)
            sub.insert(0,a)
            flat.remove(a)
        result.insert(0,sub)
    return result


# In[240]:

def check_rook(board):
    px = 0
    py = 0
    rx = 0
    ry = 0
    for row in board:
        if ('R' in row):
            rx = row.index('R')
            ry = board.index(row)
        if ('P' in row):
            px = row.index('P')
            py = board.index(row)
    return px == rx or rx == ry


# In[241]:

def rotate_matrix(matrix):
    result = []
    matrix.reverse()
    for col in range (0,len(matrix[0])):
        sub = []
        for row in matrix:
            sub.append(row[col])
        result.append(sub)
    return result


# In[242]:

def product_range(arr):
    a = arr[0][0]*arr[1][0]
    b = arr[0][0]*arr[1][1]
    c = arr[0][1]*arr[1][0]
    d = arr[0][1]*arr[1][1]
    e = arr[0][1]*arr[1][2]
    f = arr[0][2]*arr[1][1]
    g = arr[0][2]*arr[1][2]
    return max(a,b,c,d,e,f,g)-min(a,b,c,d,e,f,g)


# In[243]:
