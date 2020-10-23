import random

matrix=[["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]]


def print_board(matrix):
    for i in range(3):
        for j in range(3):
            if j!=2:
                print(matrix[i][j]+ "  | ",end="  ")
            else:
                print(matrix[i][j])
        print()


print_board(matrix)

def is_space(matrix,pos1,pos2):
    if matrix[pos1][pos2]=="_":
        return True
    return False

def playing(matrix):
    for i in range(9):

        if (i%2==0):
            PLAYER=int(input("player 1 GO: "))

            if PLAYER >= 1 and PLAYER <= 3:
                if is_space(matrix,0,PLAYER-1):
                    matrix[0][PLAYER - 1] = "X"
                else:
                    while is_space(matrix,0,PLAYER-1)==False:
                        PLAYER = int(input("player 1 GO (select non-taken space): "))
                    matrix[0][PLAYER - 1] = "X"

            elif PLAYER >= 4 and PLAYER <= 6:
                if is_space(matrix,1,PLAYER//2-1):
                    matrix[1][PLAYER//2 - 1] = "X"
                else:
                    while is_space(matrix,1,PLAYER//2-1)==False:
                        PLAYER = int(input("player 1 GO (select non-taken space): "))
                    matrix[1][PLAYER//2 - 1] = "X"


            else:
                if (PLAYER==7):
                    if is_space(matrix, 2, PLAYER//3 - 1):
                        matrix[2][PLAYER//3-2]= "X"
                    else:
                       while is_space(matrix, 2, PLAYER//3 - 1)==False:
                            PLAYER = int(input("player 1 GO (select non-taken space): "))
                       matrix[2][PLAYER // 3 - 2] = "X"

                else:
                    if is_space(matrix, 2, PLAYER // 3 - 1):
                        matrix[2][PLAYER//3 - 1] = "X"
                    else:
                        while is_space(matrix,2,PLAYER//3 -1)==False:
                            PLAYER = int(input("player 1 GO (select non-taken space): "))
                        matrix[2][PLAYER//3 - 1] = "X"



        else:

            PLAYER=int(input("Player 2 GO: "))

            if PLAYER >= 1 and PLAYER <= 3:
                if is_space(matrix, 0, PLAYER - 1):
                    matrix[0][PLAYER - 1] = "O"
                else:
                    while is_space(matrix, 0, PLAYER - 1) == False:
                        PLAYER = int(input("player 2 GO (select non-taken space): "))
                    matrix[0][PLAYER - 1] = "O"

            elif PLAYER >= 4 and PLAYER <= 6:
                if is_space(matrix, 1, PLAYER // 2 - 1):
                    matrix[1][PLAYER // 2 - 1] = "O"
                else:
                    while is_space(matrix, 1, PLAYER // 2 - 1) == False:
                        PLAYER = int(input("player 2 GO (select non-taken space): "))
                    matrix[1][PLAYER // 2 - 1] = "O"


            else:
                if (PLAYER == 7):
                    if is_space(matrix, 2, PLAYER // 3 - 1):
                        matrix[2][PLAYER // 3 - 2] = "0"
                    else:
                        while is_space(matrix, 2, PLAYER // 3 - 1)==False:
                            PLAYER = int(input("player 2 GO (select non-taken space): "))
                        matrix[2][PLAYER // 3 - 2] = "O"

                else:
                    if is_space(matrix, 2, PLAYER // 3 - 1):
                        matrix[2][PLAYER // 3 - 1] = "O"
                    else:
                        while is_space(matrix, 2, PLAYER // 3 - 1) == False:
                            PLAYER = int(input("player 2 GO (select non-taken space): "))
                        matrix[2][PLAYER // 3 - 1] = "O"

        print_board(matrix)

        if check_if_won_X(matrix)==True:
            print("X won")
            break
        if check_if_won_Y(matrix)==True:
            print_board("Y won")
            break



def check_if_won_X(matrix):
    k=0
    k1=0
    k2=0
    k3=0
    t1=0
    t2=0
    t3=0
    for i in range(len(matrix[0])):
        for j in range (len(matrix[0])):
            if  i==j-1 or i+j==len(matrix[0])-1:
                if matrix[i][j]=="X":
                    k=k+1

    for i in range (3):
        if matrix[0][i]=="X":
            k1=k1+1
        if matrix[1][i]=="X":
            k2=k2+1
        if matrix[2][i]=="X":
            k3=k3+1
        if matrix[i][0]=="X":
            t1=t1+1
        if matrix[i][1]=="X":
            t2+=t2
        if matrix[i][2]=="X":
            t3+=t3


    if k==3 or k1==3 or k2==3 or k3==3 or t1==3 or t2==3 or t3==3:
        return True

    return False

def check_if_won_Y(matrix):
    k = 0
    k1 = 0
    k2 = 0
    k3 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            if i == j - 1 or i + j == len(matrix[0]) - 1:
                if matrix[i][j] == "Y":
                    k = k + 1

    for i in range(3):
        if matrix[0][i] == "Y":
            k1 = k1 + 1
        if matrix[1][i] == "Y":
            k2 = k2 + 1
        if matrix[2][i] == "Y":
            k3 = k3 + 1
        if matrix[i][0] == "Y":
            t1 = t1 + 1
        if matrix[i][1] == "Y":
            t2 += t2
        if matrix[i][2] == "Y":
            t3 += t3

    if k == 3 or k1 == 3 or k2 == 3 or k3 == 3 or t1 == 3 or t2 == 3 or t3 == 3:
        return True

    return False





playing(matrix)
print_board(matrix)