# withdraw and depo
bal = 5000.00
while True :
  
   print("enter 1 for check bal")
   print("enter 2 for withdrawal")
   print("enter 3 for  deposite")
   print("for exit press 0")
   passwd = 1234
   pin = int("enter atm pin")

   for i in range(3):
        
     if(passwd == pin) :
        ch = int(input("enter ur choice"))
     else:
        print("incorrect pin") 
        pin = int("enter atm pin")

        
    
  

   
   if(ch==0):
            print("thanks for using ATM")
            break 
   if(ch==1):
      print("your current balance ",bal,"Rs") 
    
   if(ch==2):
      amt = float(input("enter amount for withdraw"))
      if( amt>bal):
               print("incorrect amount your balance is low",bal)
      elif(amt>0):
         bal -=amt
         print("amount credited sucessfully")
         print("withdraw amt",amt,"AC BAL Rs",bal)

   
   if(ch==3):
      amt = float(input("enter deposite amount "))
      
      if(amt>=0):
         bal +=amt
      print("withdraw amt",amt,"AC BAL Rs",bal)   
      print("amount debited sucessfully")
    
 


