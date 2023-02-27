
t=int(input("test:"))


for i in range(0,t):
    prime=[2,3,5,7,11,13,17,19,23,29,31,37,41,47]
    
    uniquePrimeFactors=[]
    primeFactors=[]
    
    n= int(input("number:"))
    if(n<2):
        print("0")
    else:
        while(n!=1):
            for j in prime:
                if n%j==0:
                    div = n/j;
                    
                    if j not in uniquePrimeFactors:
                        uniquePrimeFactors.append(j);
                    primeFactors.append(j);    
                    break;
            n=div        

    
    print(primeFactors)
    print(uniquePrimeFactors)
    print(len(uniquePrimeFactors))
