n,m = list(map(int,input().split()))
i = 1
if(n*2 > m or n*3>m):
    if(n==m):
       print("0")
    else:
       print("-1") 
else:
   while(n<m):
        if(i%2==0):
            n = n * 3
        else:
            n = n* 2
        
        if(n*2<m or n*3<m):
            i = i+1
   
   print(i)
        