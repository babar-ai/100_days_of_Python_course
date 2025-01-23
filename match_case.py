

x = int(input("choose any random number bt 0 to 5 \n"))

match x:
    
    case 0:
        print('your are very lucy')
        
    case 1:
        print("you will be marry this month")
    
    case 4:
        print("you will get job this week")
    
    #default case
    
    case _ if x!=5:
        print("you will be fail..")
    
    case _:
        print("i hope you will be fail")
        
        