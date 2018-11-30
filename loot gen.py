import random


cur_type = ["copper", "silver", "gold", "plat"]

def generator():
    x= 200
    choice = random.choice(cur_type)

    end = input()
    for i in range (10):
        if choice == "plat":
            x=5
            cur = random.randrange(1,x)
            print(cur,"plat")
            
            generator()        
        if choice == "copper":
            x=200
            cur = random.randrange(1,x)
            print(cur,"copper")
            
            generator()
        if choice == "silver":
            x=100
            cur = random.randrange(1,x)
            print(cur,"silver")
            
            generator()
        if choice == "gold":
            x=15
            cur = random.randrange(1,x)
            print(cur,"gold")
            
            generator()
generator()
