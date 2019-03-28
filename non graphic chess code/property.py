from printshow import *
#below code is for pawn of small
def pawnsm(a,b,d,e):
    e=0
    if (b[0]+1==d[0] or b[0]-1==d[0]) and b[1]+1==d[1]:
        if a[d[0]][d[1]]>0 and a[d[0]][d[1]]<7:
            killed(a,b,d)
        else:
            e=printerr(a)
    elif b[0]==d[0] and b[1]+1==d[1]:
        if a[d[0]][d[1]]==0:
            do(a,b,d)
        else:
            e=printerr(a)
    elif b[1]==1 and d[1]==3 and a[d[0]][d[1]]==0 and b[0]==d[0]:
        do(a,b,d)        
    else:
        e=printerr(a)
    return e    
def pawncap(a,b,d,e):
    e=0
    if (b[0]+1==d[0] or b[0]-1==d[0]) and b[1]-1==d[1]:
        if a[d[0]][d[1]]>6:
            killed(a,b,d)
        else:
            e=printerr(a)
    elif b[0]==d[0] and b[1]-1==d[1]:
         if a[d[0]][d[1]]==0:    
            do(a,b,d)
         else:
            e=printerr(a)
    elif b[1]==6 and d[1]==4 and b[0]==d[0] and a[d[0]][d[1]]==0:
        do(a,b,d)
    else:
        e=printerr(a)
    return e    
def horse(a,b,d,e):
    e=0
    if (abs(b[0]-d[0])==1 and abs(b[1]-d[1])==2) or (abs(b[0]-d[0])==2 and abs(b[1]-d[1])==1):
        if (a[b[0]][b[1]]==3 and a[d[0]][d[1]]>6) or (a[b[0]][b[1]]==9 and a[d[0]][d[1]]<7 and a[d[0]][d[1]]>0):
            killed(a,b,d)
        elif a[b[0]][b[1]]==3:
            if a[d[0]][d[1]]==0:
                do(a,b,d)
            else:
                e=printerr(a)
        elif a[b[0]][b[1]]==9:
            if a[d[0]][d[1]]==0:
                do(a,b,d)
            else:
                e=printerr(a)
    else:
        e=printerr(a)
    return e
def qrb(a,b,d,e):
    if (b[0]==d[0] or b[1]==d[1]) and a[b[0]][b[1]] in [2,5,8,11]:
        if b[0]==d[0]:
            if b[1]>d[1]:
                q=-1
            elif b[1]<d[1]:
                q=+1
            s=range(b[1]+q,d[1],q)
            j=0
            for i in s:
                if a[b[0]][i]!=0:
                    j=1
            if j==0:
                if (a[b[0]][b[1]] in [2,5] and a[d[0]][d[1]]>6) or (a[b[0]][b[1]] in [8,11] and a[d[0]][d[1]]<7 and a[d[0]][d[1]]>0):
                    killed(a,b,d)
                elif a[b[0]][b[1]] in [2,5,8,11] and a[d[0]][d[1]]==0:
                    do(a,b,d)
                else:
                    e=printerr(a)
            elif j==1:
                e=printerr(a)
        elif b[1]==d[1]:
            if b[0]>d[0]:
                q=-1
            elif b[0]<d[0]:
                q=+1
            s=range(b[0]+q,d[0],q)
            j=0
            for i in s:
                if a[i][b[1]]!=0:
                    j=1
            if j==0:
                if (a[b[0]][b[1]] in [2,5] and a[d[0]][d[1]]>6) or (a[b[0]][b[1]] in [8,11] and a[d[0]][d[1]]<7 and a[d[0]][d[1]]>0):
                    killed(a,b,d)
                elif a[b[0]][b[1]] in [2,5,8,11] and a[d[0]][d[1]]==0:
                    do(a,b,d)
                else:
                    e=printerr(a)
            elif j==1:
                e=printerr(a)
    elif abs(b[0]-d[0])==abs(b[1]-d[1]) and a[b[0]][b[1]] in [4,5,10,11]:
        if b[0]>d[0] and b[1]>d[1]:
            q=range(b[0]+1,d[0],1)
            r=range(b[1]+1,d[1],1)
        elif b[0]>d[0] and b[1]<d[1]:
            q=range(b[0]+1,d[0],1)
            r=range(b[1]-1,d[1],-1)
        elif b[0]<d[0] and b[1]>d[1]:
            q=range(b[0]-1,d[0],-1)
            r=range(b[1]+1,d[1],1)
        elif b[0]<d[0] and b[1]<d[1]:
            q=range(b[0]-1,d[0],-1)
            r=range(b[1]-1,d[1],-1)
        h=0
        print(q,r)
        for i in range(len(q)):
            if a[q[i]][r[i]]==0:
                h=1
        if h==0:
            if (a[b[0]][b[1]] in [4,5] and a[d[0]][d[1]] in [7,8,9,10,11,12]) or (a[b[0]][b[1]] in [10,11] and a[d[0]][d[1]] in [1,2,3,4,5,6]):
                killed(a,b,d)
            elif a[b[0]][b[1]] in [4,5,10,11] and a[d[0]][d[1]]==0:
                do(a,b,d)  
            else:
                e=printerr(a)
        elif h==1:
            e=printerr(a)
    else:
        e=printerr(a)
    return e        
def king(a,b,d,e):
    e=0
    if abs(abs(b[0])-abs(d[0]))<=1 and (abs(b[1])-abs(d[1]))<=1:
        if (a[d[0]][d[1]]>6 and a[b[0]][b[1]]==12) and (a[d[0]][d[1]]>0 and a[d[0]][d[1]]<7 and a[b[0]][b[1]]==6):
            killed(a,b,d)
        elif a[d[0]][d[1]]==0:
            do(a,b,d)
        else:
            e=printerr(a)
    else:
        e=printerr(a)
    return e











def checknmcode(a,b):
    if a[b[0]][b[1]]==1:
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
def checkname(a,b):
    if a[b[0]][b[1]]==1:
        return ' capital pawn'
    elif a[b[0]][b[1]]==2:
        return ' capital rook'
    elif a[b[0]][b[1]]==3:
        return ' capital knight'
    elif a[b[0]][b[1]]==4:
        return ' capital bishop'
    elif a[b[0]][b[1]]==5:
        return ' capital queen'
    elif a[b[0]][b[1]]==6:
        return ' capital king'
    elif a[b[0]][b[1]]==7:
        return ' small pawn'
    elif a[b[0]][b[1]]==8:
        return ' small rook'
    elif a[b[0]][b[1]]==9:
        return ' small knight'
    elif a[b[0]][b[1]]==10:
        return ' small bishop'
    elif a[b[0]][b[1]]==11:
        return ' small queen'
    elif a[b[0]][b[1]]==12:
        return ' small king'
def killed(a,b,d):
    if a[d[0]][d[1]] in [1,2,3,4,5,6]:
        g=open('capital.py','a')
    elif a[d[0]][d[1]] in [7,8,9,10,11,12]:
        g=open('small.py','a')
    g.write(checkname(a,b)+' kills'+checkname(a,d)+'\n')
    g.close()
    u=open('kills.py','r')
    o=u.read()
    u.close()
    u=open('kills.py','w')
    u.write(checknmcode(a,d)+o)
    u.close()
    s=checkname(a,d)
    a[d[0]][d[1]]=a[b[0]][b[1]]
    a[b[0]][b[1]]=0
    printshow(a)
    print(checkname(a,d)+' kills '+s+'\n\n\n')
def do(a,b,d):
    a[d[0]][d[1]]=a[b[0]][b[1]]
    a[b[0]][b[1]]=0
    printshow(a)
    print('\n\n\n')
def printerr(a):
    printshow(a)
    print('this cant be done\n\n\n')
    return 1