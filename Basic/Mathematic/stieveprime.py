def stevprime(n):
    isprime =[True for i in range(n+1)]
    isprime[0] = False
    isprime[1] = False
    i,a =2,2 
    for i in range(i,n,i*i):
        a = 2 * i
        print("i",i)
        for a in range(a,n+1):
            isprime[a] = True
            print(a)
            a = a + i
            print(a)
        
    return isprime        
    
if __name__ == "__main__":
    isprime = []
    isprime = stevprime(10)
    for i in range(10):
        print(i," =",isprime[i])