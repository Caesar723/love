def 心(n):
    for a in range(0,round(n/2+0.1)-1):
        for b in range(0,round(n/2+0.1)-1-a):
            print(" ",end="")
        print("*",end="")
        if n%2==0:
            for c in range(0,2*a):
                print(" ",end="")
            print("*",end="")
        else:
            for f in range(0,2*a-1):
                print(" ",end="")
            if a!=0:
                print("*",end="")
        for d in range(0,(round(n/2+0.1)-1-a)*2-1):
            print(" ",end="")
        print("*",end="")
        if n%2==0:
            for e in range(0,2*a):
                print(" ",end="")
            print("*",end="")
        else:
            for f in range(0, 2 * a-1):
                print(" ", end="")
            if a != 0:
                print("*", end="")
        print()
    for g in range(0,n):
        for h in range(0,g):
            print(" ",end="")
        if g!=n-1:
            print("*",end="")
        for i in range(0,2*n-3-2*g):
            if g==0:
                if i==n-2:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                print(" ",end="")
        print("*",end="")
        print()
心(6)