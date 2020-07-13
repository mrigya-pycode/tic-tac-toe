#tic tac toe

'''

#to print the board between two players
p=1
tm=0
flag=0
board=[1,2,3,
       4,5,6,
       7,8,9]




def print_board():
 print (board[0],'|',board[1],'|',board[2])
 print ('---------')
 print (board[3],'|',board[4],'|',board[5])
 print ('---------')
 print (board[6],'|',board[7],'|',board[8])



def res_check():
    if flag==1:
        print('p1 wins')
        exit()
    elif flag==2:
        print('p2 wins')
        exit()
    elif flag==3:
        if tm==9:
         print('it is a tie')
         exit()


def win_check():
     global flag
     if board[0]=='X'and board[1]=='X'and board[2]=='X':
         #print('p1 won!')
         flag=1
         res_check()




     elif board[3]=='X'and board[4]=='X'and board[5]=='X':
        # print('p1 won!')
         flag=1
         res_check()



     elif board[6]=='X'and board[7]=='X'and board[8]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[0]=='X'and board[3]=='X'and board[6]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[1]=='X'and board[4]=='X'and board[7]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[2]=='X'and board[5]=='X'and board[8]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
         #print('p1 won!')
         flag=1
         res_check()



     elif board[0]=='O'and board[1]=='O'and board[2]=='O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[3]=='O'and board[4]=='O'and board[5]=='O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[6]=='O'and board[7]=='O'and board[8]=='O':
         print('p2 won!')
         flag=2
         res_check()

     elif board[0]=='O'and board[3]=='O'and board[6]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[1]=='O'and board[4]=='O'and board[7]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[2]=='O'and board[5]=='O'and board[8]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
         #print('p2 won!')
         flag=2
         res_check()

     else:
         flag=3
         res_check()




print_board()


while tm<9:
    print()

    if p==1:
        pos=int(input('enter the position p1: '))
        if board[pos-1]!='X' and board[pos-1]!='O':
            board[pos-1]='X'
            tm+=1
            print_board()
            win_check()
            p=2

        else:
            print('oops!take a new position ')
            continue
    else:
        pos = int(input('enter the position p2: '))
        if board[pos-1] != 'X' and board[pos-1] != 'O':
            board[pos-1] = 'O'
            tm+=1
            print_board()
            win_check()
            p=1

        else:
            print('oops!take a new position ')
            continue




'''











#to print the board between player and AI

import random
p=1
tm=0
flag=0

board=[1,2,3,
       4,5,6,
       7,8,9]

def print_board():
 print (board[0],'|',board[1],'|',board[2])
 print ('---------')
 print (board[3],'|',board[4],'|',board[5])
 print ('---------')
 print (board[6],'|',board[7],'|',board[8])


def res_check():
    if flag==1:
        print('p1 wins')
        exit()
    elif flag==2:
        print('AI wins')
        exit()
    elif flag==3:
        if tm==9:
         print('it is a tie')
         exit()


def win_check():
     global flag
     if board[0]=='X'and board[1]=='X'and board[2]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[3]=='X'and board[4]=='X'and board[5]=='X':
        # print('p1 won!')
         flag=1
         res_check()


     elif board[6]=='X'and board[7]=='X'and board[8]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[0]=='X'and board[3]=='X'and board[6]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[1]=='X'and board[4]=='X'and board[7]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[2]=='X'and board[5]=='X'and board[8]=='X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[0] == 'X' and board[4] == 'X' and board[8] == 'X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
         #print('p1 won!')
         flag=1
         res_check()


     elif board[0]=='O'and board[1]=='O'and board[2]=='O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[3]=='O'and board[4]=='O'and board[5]=='O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[6]=='O'and board[7]=='O'and board[8]=='O':
         print('p2 won!')
         flag=2
         res_check()

     elif board[0]=='O'and board[3]=='O'and board[6]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[1]=='O'and board[4]=='O'and board[7]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[2]=='O'and board[5]=='O'and board[8]=='O':
         #print('p2 won!')
         flag=2
         res_check()

     elif board[0] == 'O' and board[4] == 'O' and board[8] == 'O':
         #print('p2 won!')
         flag=2
         res_check()


     elif board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
         #print('p2 won!')
         flag=2
         res_check()

     else:
         flag=3
         res_check()


print_board()


while tm<9:
    print()

    if p==1:
        pos=int(input('enter the position p1: '))
        if board[pos-1]!='X' and board[pos-1]!='O':
            board[pos-1]='X'
            tm+=1
            print_board()
            win_check()
            p=2

        else:
            print('oops!take a new position ')
            continue
    o=random.randint(1,9)
    if board[o]!='X' and board[o]!='O':
            board[o]='O'
            tm += 1
            print()
            print_board()
            win_check()
            p=1




































