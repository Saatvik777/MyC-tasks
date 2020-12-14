terms = int(input("no. of terms?"))
t1 = 0
t2 = 1
min_value = 2
if terms <= 0:
    print("invalid input")
elif terms == 1:
    print("fibonacci sequence:")
    print (t1)
else: 
    print ("fibonacci sequence:")
    print(t1,",",t2,end=',')
    while min_value < terms:
        nth = t1 + t2
        print(nth,end=',')
        t1 = t2
        t2 = nth
        min_value += 1
    
