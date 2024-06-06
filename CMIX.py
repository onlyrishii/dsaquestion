t=int(input())
for i in range(t):
    arr=[]
    num=int(input())
    for j in range(num):
        list1=list(map(int,input().split()))
        arr.append(list1) #[[1 10][5 5]]
    list2=[]
    for v in range(num):
        for a in range(v+1,num):
            value=(arr[v][0]*arr[a][1])+(arr[v][1]*arr[a][0])
            list2.append(value)
    print(max(list2))

        