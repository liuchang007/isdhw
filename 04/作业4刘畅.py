import math
class Ellipse:
    def Ellipse(self,a,b):
        return(math.pi*a*b)
class Circle:
    def Circle(self,c):
        return math.pi*c*c
class Rectangle:
    def Rectangle(self,d,e):
        return d*e
class Square:
    def Square(self,f):
        return(f*f)
class Myclass(Ellipse,Square,Rectangle,Circle):
    count=0
    def compute_area(self,shapes):
        q=[]
        p=Myclass()
        a=shapes
        b=a.split(',')
        x=0
        y=0
        while (x<len(b)):
            b[x]='p.'+b[x]
            if(ord(b[x][len(b[x])-1])>=48 and ord(b[x][len(b[x])-1])<=57):
                b[x]=b[x]+','+b[x+1]
                q.append(x+1)
                x=x+1
            x=x+1
        for j in q:
            del b[j-y]
            y=y+1
        for x in range(0,len(b)):
            exec('Myclass.count+='+b[x])
        return(Myclass.count)
q=Myclass()
print("总面积是：",q.compute_area(input("请输入图形列表，如Ellipse(16,20),Square(15),Rectangle(20,15):")))
