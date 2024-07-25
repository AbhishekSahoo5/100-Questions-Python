num=17

if num==1:
    print("Not prime")
if num>1:
    for i in range(2,num):
        if(num%i==0):
            print("Not a prime")
            break
        else:
            print("Is a prime")
            break