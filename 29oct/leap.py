year = int(input("enter year to check leap year or not "))

if(year %400==0 ) :
                 print("year is leap",year  )
elif(year%100==0) :     
                         print("not leap year is leap",year  )
elif(year%4==0)  :
                  print(" leap year ",year)   

else :     print("not a leap year ",year )   
                                              
  
