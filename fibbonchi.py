while True:
    answer_type=input('would you like to get a [f]ull fibonachi string, just a [s]ingle number, or the [a]verage of a selected part?')

    if answer_type=='f':
        amount=input('Enter how many parts to the fibonacci sequence you desire to see')

        if int(amount)==1:
            fibonacci=[0]
            print(fibonacci)
        elif int(amount)==0:
            fibonacci=[]
            print(fibonacci)
        elif int(amount)==2:
            fibonacci=[0,1]
            print(fibonacci)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(amount)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            print(fibonacci)

    elif answer_type=='s':
        single_num=input('What part to the fibonachi sequece do you wish to see')

        if int(single_num)==1:
            fibonacci=0
            print(fibonacci)
        elif int(single_num)==0:
            fibonacci='Nothing'
            print(fibonacci)
        elif int(single_num)==2:
            fibonacci=1
            print(fibonacci)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(single_num)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            print(fibonacci[int(single_num)-1])

    elif answer_type=='a':
        amount=input('How many parts to the fibonachi sequence do you wish to be averaged?')
        if int(amount)==1:
            fibonacci=0
            print(fibonacci)
        elif int(amount)==0:
            fibonacci=[]
            print(fibonacci)
        elif int(amount)==2:
            fibonacci=[0,1]
            average=.5
            print(average)
        else:
            fibonacci=[0,1,1]
            for parts in range(1,int(amount)-2):
                addative=fibonacci[-2]+fibonacci[-1]
                fibonacci.append(addative)
            average=sum(fibonacci)/len(fibonacci)
            print(average)

    else:
        print('Not a valid input.')
