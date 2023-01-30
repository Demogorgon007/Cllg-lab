print ("Enter the number of queens")
q = int(input())

cb = [[0]*q for _ in range(q)]

def cross(i, j):

    for k in range(0,q):
        if cb[i][k]==1 or cb[k][j]==1:
            return True
    #checking diagonally
    for k in range(0,q):
        for l in range(0,q):
            if (k+l==i+j) or (k-l==i-j):
                if cb[k][l]==1:
                    return True
    return False

def queens(n):
    if n==0:
        return True
    for i in range(0,q):
        for j in range(0,q):
            if (not(cross(i,j))) and (cb[i][j]!=1):
                cb[i][j] = 1
                if queens(n-1)==True:
                    return True
                cb[i][j] = 0

    return False

queens(q)
for i in cb:
    print (i)