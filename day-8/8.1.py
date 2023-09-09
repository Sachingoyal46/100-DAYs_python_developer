def primenumber(n):
   
    for i in range(2,n):
        is_prime=True
        if n%i==0:
           is_prime=False
            
    if is_prime==True:
        print("it is a prime number")
    else:
        print("it is not a prime number")    


        
primenumber(7)       