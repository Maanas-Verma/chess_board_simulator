def printshow(a):
    print(' \\')
    print('| +-----------------+')
    print('8 |',chekn(a,[0,7]),chekn(a,[1,7]),chekn(a,[2,7]),chekn(a,[3,7]),chekn(a,[4,7]),chekn(a,[5,7]),chekn(a,[6,7]),chekn(a,[7,7]),'|')
    print('7 |',chekn(a,[0,6]),chekn(a,[1,6]),chekn(a,[2,6]),chekn(a,[3,6]),chekn(a,[4,6]),chekn(a,[5,6]),chekn(a,[6,6]),chekn(a,[7,6]),'|')
    print('6 |',chekn(a,[0,5]),chekn(a,[1,5]),chekn(a,[2,5]),chekn(a,[3,5]),chekn(a,[4,5]),chekn(a,[5,5]),chekn(a,[6,5]),chekn(a,[7,5]),'|')
    print('5 |',chekn(a,[0,4]),chekn(a,[1,4]),chekn(a,[2,4]),chekn(a,[3,4]),chekn(a,[4,4]),chekn(a,[5,4]),chekn(a,[6,4]),chekn(a,[7,4]),'|')
    print('4 |',chekn(a,[0,3]),chekn(a,[1,3]),chekn(a,[2,3]),chekn(a,[3,3]),chekn(a,[4,3]),chekn(a,[5,3]),chekn(a,[6,3]),chekn(a,[7,3]),'|')
    print('3 |',chekn(a,[0,2]),chekn(a,[1,2]),chekn(a,[2,2]),chekn(a,[3,2]),chekn(a,[4,2]),chekn(a,[5,2]),chekn(a,[6,2]),chekn(a,[7,2]),'|')
    print('2 |',chekn(a,[0,1]),chekn(a,[1,1]),chekn(a,[2,1]),chekn(a,[3,1]),chekn(a,[4,1]),chekn(a,[5,1]),chekn(a,[6,1]),chekn(a,[7,1]),'|')
    print('1 |',chekn(a,[0,0]),chekn(a,[1,0]),chekn(a,[2,0]),chekn(a,[3,0]),chekn(a,[4,0]),chekn(a,[5,0]),chekn(a,[6,0]),chekn(a,[7,0]),'|')
    print('| +-----------------+')
    print('+---1-2-3-4-5-6-7-8--->')
    a=open('kills.py','r')
    print(a.read())
    a.close()
def chekn(a,b):
    if a[b[0]][b[1]]==0:
        return '*'
    elif a[b[0]][b[1]]==1:
        return 'P'
    elif a[b[0]][b[1]]==2:
        return 'R'
    elif a[b[0]][b[1]]==3:
        return 'H'
    elif a[b[0]][b[1]]==4:
        return 'B'
    elif a[b[0]][b[1]]==5:
        return 'Q'
    elif a[b[0]][b[1]]==6:
        return 'K'
    elif a[b[0]][b[1]]==7:
        return 'p'
    elif a[b[0]][b[1]]==8:
        return 'r'
    elif a[b[0]][b[1]]==9:
        return 'h'
    elif a[b[0]][b[1]]==10:
        return 'b'
    elif a[b[0]][b[1]]==11:
        return 'q'
    elif a[b[0]][b[1]]==12:
        return 'k'