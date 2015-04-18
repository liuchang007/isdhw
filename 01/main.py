for i in range(1,10):
        for j in range(i,10):
            w=str.format("{0:1}*{1:1}={2:>2}",i,j,i*j)
            print(w,end="  ")
        print()
for i in range(1,10):
        for k in range(0,i-1):
            print(end="        ")
        for j in range(i,10):
            m=str.format("{0:1}*{1:1}={2:>2}",i,j,i*j) 
            print(m,end="  ")
        print()

