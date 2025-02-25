# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: 2051623      iit id 20230311
# Date: 13/12/2023
# UKWATTA LIYANAGE YASHITH CHANDEEPA GIMNATH




#for students

CreditRange = [120,100,80,60,40,20,0]

while True:
 try:
   passCredit = int(input("Please enter your Credits at pass: "))
   deferCredit = int(input("Please enter your Credits at defer: "))
   failCredit = int(input("Please enter your Credits at fail: "))
   Total = passCredit + deferCredit + failCredit
   NotinRange = (passCredit not in CreditRange) or (deferCredit not in CreditRange) or (failCredit not in CreditRange)

   if passCredit == 120:
        Outcome = "-Progress-"
        
   elif passCredit == 100 and ((deferCredit == 0 and failCredit == 20) or (failCredit == 0 and deferCredit == 20)):
       Outcome = "-Progress Module Trailer-"
       
   elif passCredit <= 40 and failCredit >= 80:
        Outcome = "-Exclude-"
        
   else:
        Outcome = "-Do not Progress(module retriever)-"
   print(Outcome)
   print("")
   break

   if Total !=120:
        print("-Total Incorrect-")
        continue
        
   
   if  NotinRange:
        print("-Not in Range-")
        continue
    

 except ValueError :
    Outcome = "-Integer Required-"
    print(Outcome)
    continue

    
