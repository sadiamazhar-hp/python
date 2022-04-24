##Reusable Function to Display the Matrix
def diplaymatrix(M):
    Nr = len(M)
    nC = len(M[0])
    for r in range(Nr):
        for c in range(Nc):
            print(( M[r][c]),end="\t")
    print("-----------------------------------------------")
##Unput augmented matrix
Nr = int(input("enter no. of rows : "))
Nc = int(input("enter no. of columns : "))
##Input matrix element
M = []
for r in range(Nr):
    R = []
    for c in range(Nc):
        Element = float(input("enter matrix element : "))
        R.append(Element)
    M.append(R)
diplaymatrix(M)
##Input pivot Element
Pr = int(input("enter row no. of pivot element:  "))
Pc = int(input("enter column no. of pivot element:  "))
Pr -= 1
Pc -= 1
while(Pr >= 0 or Pc >= 0):
    ##Make pivot element = 1 using elementary row operations
    ##Divide each element of pivot row by pivot element
    PivotElement = M[Pr][Pc]
    for c in range(Nc):
        M[Pr][c] = M[Pr][c]/PivotElement
    diplaymatrix(M)
    ##Make other values in pivot column = 0 using elementary row operations
    ## Multiply each element of pivot row by pivot value and subtract it from
    ##corresponding elemant of row under consideration
    for r in range(Nr):
        if(r==Pr):
            continue
        PivotValue = M[r][Pc]
        for c in range(Nc):
            M[r][c] = M[r][c] - M[Pr][c]*PivotValue
    diplaymatrix(M)
    Pr = int(input("enter row no. of pivot element:  "))
    Pc = int(input("enter column no. of pivot element:  "))        
    Pr -= 1
    Pc -= 1
