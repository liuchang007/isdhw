def f(x,i):
    y=0
    z=False
    low=0
    high=len(x)-1
    while(low<(high-1)):
        mid=int((low+high)/2)
        if(x[high]==i):
            y=high
            z=True
            break
        if(x[low]==i):
            y=low
            z=True
            break
        if(x[mid]==i):
            y=mid
            z=True
            break
        elif(x[mid]>i):
            high=mid
        elif(x[mid]<i):
            low=mid
    if(z):
        return(y)

    else:
        return(0)
stu=input("请输入要查找的序列，用逗号隔开，如 a，b，c，d 按照从小到大顺序：")
stu1=eval(stu)
stu2=list(stu1)
x=stu2
i=int(input("请输入你要找到数字："))
y=f(x,i)
if y==0:
    print('无法找到')
else:
    print("找到，你要找的数在列表中的第{0}个位置".format(y))
    

