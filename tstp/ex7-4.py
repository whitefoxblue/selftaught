prime = [3,5,7,13]
while input('Enter q to quit or any key to continue: ') != 'q':
#    prime = [3,5,7,13]
    i = 0
    flag = False
    
#    number = int(input("Enter a prime number: "))
    
    while flag == False:
#        if i == len(prime):
#            print("That is not correct")
#            flag = True
#        elif number == prime[i]:
#            print("You found a number")
#            flag = True
#        else:
#            i += 1
        try:
            number = int(input("Enter a prime number: "))
            if number in prime:
                print("You found a number.")
                flag = True
            else:
                print("That is is not correct.")
                flag = True
        except ValueError:
            print("A number please")

    
    
                 
        
             
             
      
      
      
