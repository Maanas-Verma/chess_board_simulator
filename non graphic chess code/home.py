from printshow import *
from property import *
ki=open('kills.py','w')
ki.write('')
ki.close()
ki=open('small.py','w')
ki.write('')
ki.close()
ki=open('capital.py','w')
ki.write('')
ki.close()
def checkcode(a,b,d,e):
    if a[b[0]][b[1]]==1:
        return pawncap(a,b,d,e)
    elif a[b[0]][b[1]] in [2,4,5,8,10,11]:
        return qrb(a,b,d,e)
    elif a[b[0]][b[1]] in [3,9]:
        return horse(a,b,d,e)
    elif a[b[0]][b[1]]%6==0 and a[b[0]][b[1]]!=0:
        return king(a,b,d,e)
    elif a[b[0]][b[1]]==7:
        return pawnsm(a,b,d,e)
def tryint(lp):
    try:
        int(lp)
        if int(lp)>8:
            printshow(a)
            print("coordinates are out of range\n\n\n")
            return False
        else:
            return True
    except ValueError:
        printshow(a)
        print('coorinates are not entered correctly\n\n\n')
        return False
def checkcapital(d):
    b=a[d[0]][d[1]]
    if b==0:
        return 0
    elif b in [7,8,9,10,11,12]:
        return 0
    elif b in [1,2,3,4,5,6]:
        print("sorry there is already an element of capital")
        return 's'
def checksmall(d):
    b=a[d[0]][d[1]]
    if b==0:
        return 0
    elif b in [1,2,3,4,5,6]:
        return 0
    elif b in [7,8,9,10,11,12]:
        print("sorry there is already an element of small")
        return 's'
a=[[8, 7, 0, 0, 0, 0, 1, 2],
 [9, 7, 0, 0, 0, 0, 1, 3],
 [10, 7, 0, 0, 0, 0, 1, 4],
 [11, 7, 0, 0, 0, 0, 1, 5],
 [12, 7, 0, 0, 0, 0, 1, 6],
 [10, 7, 0, 0, 0, 0, 1, 4],
 [9, 7, 0, 0, 0, 0, 1, 3],
 [8, 7, 0, 0, 0, 0, 1, 2]]
c=1
printshow(a)
print('\n\n\n')
while True:
    d=0
    while d==0:
        e=0
        if c==1:
            print('its chance of capital')
        if c==0:
            print('its chance of small')
        s=input('enter codes : ')
        if len(s)==4 and tryint(s[0]) and tryint(s[1]) and tryint(s[2]) and tryint(s[3]):
            c=(c+1)%2
            b=[int(s[0])-1,int(s[1])-1]
            d=[int(s[2])-1,int(s[3])-1]
            if c==0 and a[b[0]][b[1]]>6:
                printshow(a)
                print('there is no element of capital\n\n\n')
                c=(c+1)%2
            elif c==1 and a[b[0]][b[1]]<=6 and a[b[0]][b[1]]!=0:
                printshow(a)
                print('there is no element of small\n\n\n')
                c=(c+1)%2
            elif a[b[0]][b[1]]==0:
                printshow(a)
                print('there is no element here\n\n\n')
                c=(c+1)%2
            elif (a[b[0]][b[1]]<=6 and c==0) or (a[b[0]][b[1]]>6 and c==1):
                e=checkcode(a,b,d,e)
                if e==1:
                    c=(c+1)%2
        elif s=='endgame':
            d=3
        else:
            printshow(a)
            print('if you exit game write endgame\n\n\n')
        bam=[]
        bal=[]
        for i in a:
            bam.append(6 in i)
            bal.append(12 in i)
        if (True not in bam) or (True not in bal):
            d=3
    if d==3:
        c=open('kills.py','r')
        d=c.read()
        print('+---------------------------------------------------------------')
        print('|  Here the game ends                ')
        print('|                                    ')
        print('|  Elementes killed in this game are ')
        print('|                                    ')
        print('|  \''+d+'\'')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|')
        print('|  Press enter to exit  ')
        print('+---------------------------------------------------------------')
        oehd=input('enter codes : ')
        c.close()
        c=open('kills.py','w')
        c.write()
        c.close()
        c=open('small.py','w')
        c.write()
        c.close()
        c=open('capital.py','w')
        c.write()
        c.close()
        break