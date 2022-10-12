def add(P, Q):    
   return P + Q   
def subtract(P, Q):   
   return P - Q   
def multiply(P, Q):   
   return P * Q   
def divide(P, Q):   
   return P / Q     

li=['a','b','c','d']
a=1
while(a==1):
    print("\n***********************CALCULATOR***********************")
    choice = input("\nPress\na for addition\nb for subtraction\nc for multiplication\nd for division\ne for exit\n")
    if choice =='e':
        print("Exiting!!!")
        break
    if choice not in li:
        print("Please enter a valid choice")
        continue
    P = int (input ("Please enter the first number: "))    
    Q = int (input ("Please enter the second number: "))
    if choice == 'a':    
       print (P, " + ", Q, " = ", add(P, Q))    
        
    elif choice == 'b':    
       print (P, " - ", Q, " = ", subtract(P, Q))    
        
    elif choice == 'c':    
       print (P, " * ", Q, " = ", multiply(P, Q))    
    elif choice == 'd':    
       print (P, " / ", Q, " = ", divide(P, Q))

