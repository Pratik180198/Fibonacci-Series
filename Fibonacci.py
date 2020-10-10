num1=input("Enter Integer: ")
try:
    num=int(num1)
    def fibonacci(num):
        if num==0:
            return 0
        elif num==1:
            return 1
        else:
            return fibonacci(num-1)+fibonacci(num-2)
    for num in range(num):
        print(fibonacci(num),end=' ')    
except:
    print("Enter Integer only")
    