def Z_M(Nr,Nc):
    j=[]
    b=0
    o=Nr-1
    while o>=0:
        j.append(b)
        o-=1
    k=[]
    i=0
    while i<=Nc-1:
        k.append(j.copy())
        i+=1
    return k
def M_tr(matrix):
##    print(matrix)
    Nr=len(matrix)
    Nc=len(matrix[0])
    Result=Z_M(Nr,Nc)
    for i in range(Nr):
        for j in range(Nc):
            Result[j][i]= matrix[i][j]
    return Result

def Z_m(Nr,Nc):
    j=[]
    b=0
    o=Nc-1
    while o>=0:
        j.append(b)
        o-=1
    k=[]
    i=0
    while i<=Nr-1:
        k.append(j.copy())
        i+=1
    return k

def M_add(mx1,mx2):
    Nr=len(mx1)
    Nc=len(mx2[0])
    result=Z_m(Nr,Nc)
    for i in range(Nr):
        for j in range(Nc):
            result[i][j]= mx1[i][j] + mx2[i][j]
    return result

def M_mult(mx1,mx2):
    Nr1=len(mx1)
    Nc1=len(mx1[0])
    Nr2=len(mx2)
    Nc2=len(mx2[0])
    result=Z_m(Nr1,Nc2)
    if Nc1==Nr2:
        for i in range(Nr1):
            for j in range(Nc2):
                for k in range(Nr2):
                    result[i][j]= mx1[i][k] + mx2[k][j]
    else:
        print('No of columns of matrix 1 should be equal to No of rows of matrix 2')
    return result
def Sort_(M):
    Nr=len(M)
    Nc=len(M[0])
    for i in range(Nr):
        for j in range(Nc):
            for k in range(Nr):
                for l in range(Nc):
                    if M[i][j]<M[k][l]:
                        M[k][l], M[i][j]=M[i][j],M[k][l]
    print("Your sorted Matrix is:")
    return M
    
